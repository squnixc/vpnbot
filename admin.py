import asyncio
import datetime as dt
import inspect
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import psutil

from config import config
from db import execute, fetchall, fetchone
from settings import VERSION, TARIFFS, LIMITS
from utils.storage import all_user_ids, is_banned

router = Router()


def is_admin(user_id: int) -> bool:
    return user_id in config.admin_ids


def admin_only(handler):
    sig = inspect.signature(handler)

    async def wrapper(message: types.Message, *a, **kw):
        if not is_admin(message.from_user.id):
            await message.answer("⛔ Недостаточно прав.")
            return
        filtered = {k: v for k, v in kw.items() if k in sig.parameters}
        return await handler(message, *a, **filtered)

    return wrapper


def admin_only_callback(handler):
    sig = inspect.signature(handler)

    async def wrapper(callback: types.CallbackQuery, *a, **kw):
        if not is_admin(callback.from_user.id):
            await callback.message.answer("⛔ Недостаточно прав.")
            await callback.answer()
            return
        filtered = {k: v for k, v in kw.items() if k in sig.parameters}
        return await handler(callback, *a, **filtered)

    return wrapper


class SendState(StatesGroup):
    to_one_id = State()
    to_one_text = State()
    to_all_text = State()


class GiftState(StatesGroup):
    to_one_id = State()
    to_one_hours = State()
    to_all_hours = State()
    confirm = State()


class ManageState(StatesGroup):
    ban_id = State()
    unban_id = State()
    config_id = State()


def admin_panel_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📊 Статистика", callback_data="stats:show"),
                InlineKeyboardButton(text="📈 Трафик", callback_data="traffic:menu"),
            ],
            [
                InlineKeyboardButton(text="💻 Sysinfo", callback_data="sysinfo:show"),
                InlineKeyboardButton(text="ℹ️ About", callback_data="about:show"),
            ],
            [
                InlineKeyboardButton(text="✉️ Рассылки", callback_data="send:menu"),
                InlineKeyboardButton(text="🎁 Подарки", callback_data="gift:menu"),
            ],
            [InlineKeyboardButton(text="⚙️ Управление", callback_data="manage:menu")],
        ]
    )


def back_admin_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="⬅️ Назад", callback_data="admin:panel")]]
    )


def traffic_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="1d", callback_data="traffic:1d"),
                InlineKeyboardButton(text="7d", callback_data="traffic:7d"),
                InlineKeyboardButton(text="30d", callback_data="traffic:30d"),
            ],
            [InlineKeyboardButton(text="⬅️ Назад", callback_data="admin:panel")],
        ]
    )


def send_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="To one", callback_data="send:to_one"), InlineKeyboardButton(text="To all", callback_data="send:to_all")],
            [InlineKeyboardButton(text="⬅️ Назад", callback_data="admin:panel")],
        ]
    )


def gift_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="To one", callback_data="gift:to_one"), InlineKeyboardButton(text="To all", callback_data="gift:to_all")],
            [InlineKeyboardButton(text="⬅️ Назад", callback_data="admin:panel")],
        ]
    )


def manage_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Ban", callback_data="manage:ban"), InlineKeyboardButton(text="Unban", callback_data="manage:unban")],
            [InlineKeyboardButton(text="Config", callback_data="manage:config")],
            [InlineKeyboardButton(text="⬅️ Назад", callback_data="admin:panel")],
        ]
    )


def confirm_kb(action: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="✅ Подтвердить", callback_data=f"{action}:confirm"),
                InlineKeyboardButton(text="❌ Отмена", callback_data=f"{action}:cancel"),
            ]
        ]
    )


@router.message(Command("admin_panel"))
@admin_only
async def cmd_admin_panel(message: types.Message) -> None:
    await message.answer("🛠 Админ-панель", reply_markup=admin_panel_kb())


@router.callback_query(lambda c: c.data == "admin:panel")
@admin_only_callback
async def cb_admin_panel(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text("🛠 Админ-панель", reply_markup=admin_panel_kb())
    await callback.answer()


async def _stats_text() -> str:
    total_row = await fetchone("SELECT COUNT(*) AS cnt FROM users")
    active_row = await fetchone(
        "SELECT COUNT(DISTINCT user_id) AS cnt FROM subscriptions WHERE status='active' AND expires_at > NOW()"
    )
    plans = await fetchall(
        "SELECT plan, COUNT(*) AS cnt FROM subscriptions WHERE status='active' AND expires_at > NOW() GROUP BY plan"
    )
    churn_row = await fetchone(
        """
        SELECT COUNT(*) AS cnt
        FROM subscriptions
        WHERE expires_at::date >= (CURRENT_DATE - INTERVAL '7 days')
          AND expires_at::date < CURRENT_DATE
          AND status IN ('expired','canceled')
        """
    )
    total = total_row["cnt"] if total_row else 0
    active_users = active_row["cnt"] if active_row else 0
    churn = churn_row["cnt"] if churn_row else 0
    plan_lines = "\n".join([f"- {row['plan']}: {row['cnt']}" for row in plans]) or "-"
    return (
        f"👥 Всего: {total}\n"
        f"✅ Активные: {active_users}\n"
        f"📦 По тарифам:\n{plan_lines}\n"
        f"📉 Ушли (7д): {churn}"
    )


@router.message(Command("stats"))
@admin_only
async def cmd_stats(message: types.Message) -> None:
    try:
        text = await _stats_text()
        await message.answer(text, reply_markup=back_admin_kb())
    except Exception as e:
        await message.answer(f"❌ Ошибка: {e}")


@router.callback_query(lambda c: c.data == "stats:show")
@admin_only_callback
async def cb_stats(callback: types.CallbackQuery) -> None:
    try:
        text = await _stats_text()
    except Exception as e:
        text = f"❌ Ошибка: {e}"
    await callback.message.edit_text(text, reply_markup=back_admin_kb())
    await callback.answer()


async def _traffic_text(days: int) -> str:
    if days == 1:
        row = await fetchone(
            "SELECT COALESCE(SUM(bytes_up),0) AS up, COALESCE(SUM(bytes_down),0) AS down FROM traffic_daily WHERE date = CURRENT_DATE"
        )
    else:
        row = await fetchone(
            """
            SELECT COALESCE(SUM(bytes_up),0) AS up, COALESCE(SUM(bytes_down),0) AS down
            FROM traffic_daily
            WHERE date >= CURRENT_DATE - (%s * INTERVAL '1 day')
            """,
            days,
        )
    up = row["up"] if row else 0
    down = row["down"] if row else 0
    up_mb = up / 1024 / 1024
    down_mb = down / 1024 / 1024
    total_mb = up_mb + down_mb
    return f"Up: {up_mb:.2f} MB | Down: {down_mb:.2f} MB | Total: {total_mb:.2f} MB"


@router.message(Command("traffic"))
@admin_only
async def cmd_traffic(message: types.Message) -> None:
    parts = message.text.split()
    period = parts[1] if len(parts) > 1 else "1d"
    days_map = {"1d": 1, "7d": 7, "30d": 30}
    days = days_map.get(period, 1)
    try:
        text = await _traffic_text(days)
        await message.answer(text)
    except Exception as e:
        await message.answer(f"❌ Ошибка: {e}")

@router.callback_query(lambda c: c.data.startswith("traffic"))
@admin_only_callback
async def cb_traffic(callback: types.CallbackQuery) -> None:
    if callback.data == "traffic:menu":
        await callback.message.edit_text("Выберите период:", reply_markup=traffic_kb())
        await callback.answer()
        return
    _, period = callback.data.split(":")
    days_map = {"1d": 1, "7d": 7, "30d": 30}
    days = days_map.get(period, 1)
    try:
        text = await _traffic_text(days)
    except Exception as e:
        text = f"❌ Ошибка: {e}"
    await callback.message.edit_text(text, reply_markup=traffic_kb())
    await callback.answer()



def _sysinfo_text() -> str:
    boot = dt.datetime.fromtimestamp(psutil.boot_time())
    uptime = dt.datetime.now() - boot
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    return (
        f"⏱ Uptime: {uptime}\n"
        f"💽 CPU: {cpu}%\n"
        f"📦 RAM: {mem}%\n"
        f"💾 Disk: {disk}%"
    )

@router.message(Command("sysinfo"))
@admin_only
async def cmd_sysinfo(message: types.Message) -> None:
    try:
        text = _sysinfo_text()
        await message.answer(text, reply_markup=back_admin_kb())
    except Exception as e:
        await message.answer(f"❌ Ошибка: {e}")

@router.callback_query(lambda c: c.data == "sysinfo:show")
@admin_only_callback
async def cb_sysinfo(callback: types.CallbackQuery) -> None:
    try:
        text = _sysinfo_text()
    except Exception as e:
        text = f"❌ Ошибка: {e}"
    await callback.message.edit_text(text, reply_markup=back_admin_kb())
    await callback.answer()
@router.message(Command("about"))
@admin_only
async def cmd_about(message: types.Message) -> None:
    text = _about_text()
    await message.answer(text, reply_markup=back_admin_kb())


@router.callback_query(lambda c: c.data == "about:show")
@admin_only_callback
async def cb_about(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(_about_text(), reply_markup=back_admin_kb())
    await callback.answer()


def _about_text() -> str:
    tariffs = ", ".join([f"{k}: {v}" for k, v in TARIFFS.items()]) or "-"
    limits = ", ".join([f"{k}: {v}" for k, v in LIMITS.items()]) or "-"
    return f"Тарифы:  {tariffs}\nЛимиты:  {limits}\n\nВерсия: {VERSION}"


async def _send_to_one(bot, uid: int, text: str) -> bool:
    try:
        await bot.send_message(uid, text)
        return True
    except Exception:
        return False


@router.callback_query(lambda c: c.data.startswith("send"))
@admin_only_callback
async def cb_send(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == "send:menu":
        await callback.message.edit_text("Рассылки:", reply_markup=send_kb())
        await callback.answer()
        return
    if callback.data == "send:to_one":
        await callback.message.answer("Введите tg_id получателя:")
        await state.set_state(SendState.to_one_id)
    elif callback.data == "send:to_all":
        await callback.message.answer("Введите текст рассылки:")
        await state.set_state(SendState.to_all_text)
    await callback.answer()


@router.message(SendState.to_one_id)
@admin_only
async def send_to_one_id(message: types.Message, state: FSMContext) -> None:
    try:
        uid = int(message.text)
        await state.update_data(uid=uid)
        await message.answer("Введите текст сообщения:")
        await state.set_state(SendState.to_one_text)
    except ValueError:
        await message.answer("❌ Ошибка: неверный id")


@router.message(SendState.to_one_text)
@admin_only
async def send_to_one_text(message: types.Message, state: FSMContext) -> None:
    data = await state.get_data()
    uid = data.get("uid")
    ok = await _send_to_one(message.bot, uid, message.text)
    await message.answer("✅ Отправлено" if ok else "❌ Ошибка отправки")
    await state.clear()


@router.message(SendState.to_all_text)
@admin_only
async def send_to_all_text(message: types.Message, state: FSMContext) -> None:
    text = message.text
    ids = [uid for uid in all_user_ids() if not is_banned(uid)]
    sent = failed = 0
    for uid in ids:
        if await _send_to_one(message.bot, uid, text):
            sent += 1
        else:
            failed += 1
        await asyncio.sleep(0.05)
    await message.answer(f"✅ {sent} / ❌ {failed}")
    await state.clear()


async def _ensure_user_record(tg_user_id: int) -> int:
    row = await fetchone("SELECT id FROM users WHERE tg_user_id=%s", tg_user_id)
    if row:
        return row["id"]
    await execute(
        "INSERT INTO users (tg_user_id) VALUES (%s) ON CONFLICT (tg_user_id) DO NOTHING",
        tg_user_id,
    )
    row = await fetchone("SELECT id FROM users WHERE tg_user_id=%s", tg_user_id)
    if not row:
        raise RuntimeError("Failed to ensure user record")
    return row["id"]


async def _set_ban_status(tg_user_id: int, banned: bool) -> None:
    await execute(
        "INSERT INTO users (tg_user_id) VALUES (%s) ON CONFLICT (tg_user_id) DO NOTHING",
        tg_user_id,
    )
    await execute("UPDATE users SET is_banned=%s WHERE tg_user_id=%s", banned, tg_user_id)


async def _gift(user_id: int, hours: int) -> dt.datetime:
    db_id = await _ensure_user_record(user_id)
    now = dt.datetime.now(dt.timezone.utc)
    sub = await fetchone(
        """
        SELECT id, expires_at
        FROM subscriptions
        WHERE user_id=%s AND status='active' AND expires_at > NOW()
        ORDER BY expires_at DESC
        LIMIT 1
        """,
        db_id,
    )
    add = dt.timedelta(hours=hours)
    if sub and sub.get("expires_at"):
        expires_at = sub["expires_at"]
        if expires_at.tzinfo is None:
            expires_at = expires_at.replace(tzinfo=dt.timezone.utc)
        if expires_at < now:
            expires_at = now
        new_exp = expires_at + add
        await execute("UPDATE subscriptions SET expires_at=%s WHERE id=%s", new_exp, sub["id"])
    else:
        new_exp = now + add
        await execute(
            "INSERT INTO subscriptions (user_id, plan, status, expires_at) VALUES (%s,%s,%s,%s)",
            db_id,
            "gift",
            "active",
            new_exp,
        )
    return new_exp


@router.callback_query(lambda c: c.data.startswith("gift:"))
@admin_only_callback
async def cb_gift(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == "gift:menu":
        await callback.message.edit_text("Подарки:", reply_markup=gift_kb())
        await callback.answer()
        return
    if callback.data == "gift:to_one":
        await callback.message.answer("Введите tg_id пользователя:")
        await state.set_state(GiftState.to_one_id)
    elif callback.data == "gift:to_all":
        await callback.message.answer("Введите кол-во часов:")
        await state.set_state(GiftState.to_all_hours)
    await callback.answer()


@router.message(GiftState.to_one_id)
@admin_only
async def gift_to_one_id(message: types.Message, state: FSMContext) -> None:
    try:
        uid = int(message.text)
        await state.update_data(uid=uid)
        await message.answer("Сколько часов подарить?:")
        await state.set_state(GiftState.to_one_hours)
    except ValueError:
        await message.answer("❌ Ошибка: неверный id")


@router.message(GiftState.to_one_hours)
@admin_only
async def gift_to_one_hours(message: types.Message, state: FSMContext) -> None:
    data = await state.get_data()
    try:
        hours = int(message.text)
        uid = data.get("uid")
        new_exp = await _gift(uid, hours)
        await message.answer(f"🎁 До: {new_exp:%Y-%m-%d %H:%M}")
        await state.clear()
    except ValueError:
        await message.answer("❌ Ошибка: неверное число")


@router.message(GiftState.to_all_hours)
@admin_only
async def gift_to_all_hours(message: types.Message, state: FSMContext) -> None:
    try:
        hours = int(message.text)
        await state.update_data(hours=hours)
        await message.answer("Подтвердите раздачу всем", reply_markup=confirm_kb("giftall"))
        await state.set_state(GiftState.confirm)
    except ValueError:
        await message.answer("❌ Ошибка: неверное число")


@router.callback_query(lambda c: c.data.startswith("giftall"))
@admin_only_callback
async def cb_gift_all(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data.endswith("cancel"):
        await callback.message.answer("Отменено")
        await state.clear()
        await callback.answer()
        return
    data = await state.get_data()
    hours = data.get("hours", 0)
    ids = all_user_ids()
    applied = 0
    for uid in ids:
        await _gift(uid, hours)
        applied += 1
    await callback.message.answer(f"✅ Применено: {applied}")
    await state.clear()
    await callback.answer()


@router.callback_query(lambda c: c.data.startswith("manage"))
@admin_only_callback
async def cb_manage(callback: types.CallbackQuery, state: FSMContext) -> None:
    if callback.data == "manage:menu":
        await callback.message.edit_text("Управление:", reply_markup=manage_kb())
        await callback.answer()
        return
    if callback.data == "manage:ban":
        await callback.message.answer("ID для бана:")
        await state.set_state(ManageState.ban_id)
    elif callback.data == "manage:unban":
        await callback.message.answer("ID для разбан:")
        await state.set_state(ManageState.unban_id)
    elif callback.data == "manage:config":
        await callback.message.answer("ID для выдачи конфига:")
        await state.set_state(ManageState.config_id)
    await callback.answer()


@router.message(ManageState.ban_id)
@admin_only
async def manage_ban(message: types.Message, state: FSMContext) -> None:
    try:
        uid = int(message.text)
        await _set_ban_status(uid, True)
        await message.answer("🚫 Забанен")
    except ValueError:
        await message.answer("❌ Ошибка")
    await state.clear()


@router.message(ManageState.unban_id)
@admin_only
async def manage_unban(message: types.Message, state: FSMContext) -> None:
    try:
        uid = int(message.text)
        await _set_ban_status(uid, False)
        await message.answer("✅ Разбанен")
    except ValueError:
        await message.answer("❌ Ошибка")
    await state.clear()


@router.message(ManageState.config_id)
@admin_only
async def manage_config(message: types.Message, state: FSMContext) -> None:
    try:
        uid = int(message.text)
        await message.bot.send_message(uid, "Конфиг выдан 📄")
        await message.answer("Конфиг отправлен 📄")
    except Exception as e:
        await message.answer(f"❌ Ошибка: {e}")
    await state.clear()


@router.message(Command("send_to_one"))
@admin_only
async def cmd_send_to_one(message: types.Message) -> None:
    parts = message.text.split(maxsplit=2)
    if len(parts) < 3:
        await message.answer("❌ Ошибка: /send_to_one <tg_id> <текст>")
        return
    try:
        uid = int(parts[1])
    except ValueError:
        await message.answer("❌ Ошибка: tg_id")
        return
    ok = await _send_to_one(message.bot, uid, parts[2])
    await message.answer("✅" if ok else "❌ Ошибка отправки")


@router.message(Command("send_to_all"))
@admin_only
async def cmd_send_to_all(message: types.Message) -> None:
    text = message.text.partition(' ')[2]
    if not text:
        await message.answer("❌ Ошибка: нет текста")
        return
    ids = [uid for uid in all_user_ids() if not is_banned(uid)]
    sent = failed = 0
    for uid in ids:
        if await _send_to_one(message.bot, uid, text):
            sent += 1
        else:
            failed += 1
        await asyncio.sleep(0.05)
    await message.answer(f"✅ {sent} / ❌ {failed}")


@router.message(Command("gift_to_one"))
@admin_only
async def cmd_gift_to_one(message: types.Message) -> None:
    parts = message.text.split()
    if len(parts) < 3:
        await message.answer("❌ Ошибка: /gift_to_one <tg_id> <часов>")
        return
    try:
        uid = int(parts[1])
        hours = int(parts[2])
    except ValueError:
        await message.answer("❌ Ошибка: параметры")
        return
    new_exp = await _gift(uid, hours)
    await message.answer(f"🎁 До: {new_exp:%Y-%m-%d %H:%M}")


@router.message(Command("gift_to_all"))
@admin_only
async def cmd_gift_to_all(message: types.Message, state: FSMContext) -> None:
    parts = message.text.split()
    if len(parts) < 2:
        await message.answer("❌ Ошибка: /gift_to_all <часов>")
        return
    try:
        hours = int(parts[1])
    except ValueError:
        await message.answer("❌ Ошибка: число")
        return
    await state.update_data(hours=hours)
    await message.answer("Подтвердите раздачу всем", reply_markup=confirm_kb("giftall"))
    await state.set_state(GiftState.confirm)


@router.message(Command("config"))
@admin_only
async def cmd_config(message: types.Message) -> None:
    parts = message.text.split()
    if len(parts) < 2:
        await message.answer("❌ Ошибка: /config <tg_id>")
        return
    try:
        uid = int(parts[1])
        await message.bot.send_message(uid, "Конфиг выдан 📄")
        await message.answer("Конфиг отправлен 📄")
    except Exception as e:
        await message.answer(f"❌ Ошибка: {e}")


@router.message(Command("ban"))
@admin_only
async def cmd_ban(message: types.Message) -> None:
    parts = message.text.split()
    if len(parts) < 2:
        await message.answer("❌ Ошибка: /ban <tg_id>")
        return
    try:
        uid = int(parts[1])
        await _set_ban_status(uid, True)
        await message.answer("🚫 Забанен")
    except ValueError:
        await message.answer("❌ Ошибка")


@router.message(Command("unban"))
@admin_only
async def cmd_unban(message: types.Message) -> None:
    parts = message.text.split()
    if len(parts) < 2:
        await message.answer("❌ Ошибка: /unban <tg_id>")
        return
    try:
        uid = int(parts[1])
        await _set_ban_status(uid, False)
        await message.answer("✅ Разбанен")
    except ValueError:
        await message.answer("❌ Ошибка")

