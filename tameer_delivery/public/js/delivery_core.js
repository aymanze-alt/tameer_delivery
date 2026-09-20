/* Tameer Delivery — shared core: i18n, API, helpers, toast */
window.TD = window.TD || {};

TD.keys = {
	"app.name": { en: "Tameer Delivery", ar: "تعمير توصيل" },
	"tracking.title": { en: "Tameer Delivery — Live Tracking", ar: "تعمير توصيل — تتبع مباشر" },
	"app.tag": { en: "Shipment delivery & tracking", ar: "توصيل وتتبع الشحنات" },
	"nav.menu": { en: "Menu", ar: "القائمة" },
	"greet.hi": { en: "Hello", ar: "مرحباً" },
	"greet.sub": { en: "Here are your deliveries for today", ar: "هذه شحناتك المطلوب توصيلها" },
	"stat.all": { en: "All", ar: "الكل" },
	"stat.pending": { en: "Pending", ar: "معلّقة" },
	"stat.transit": { en: "In Transit", ar: "قيد التوصيل" },
	"stat.delivered": { en: "Delivered", ar: "تم التوصيل" },
	"stat.failed": { en: "Failed", ar: "فشل التوصيل" },
	"shipment": { en: "Shipment", ar: "شحنة" },
	"customer": { en: "Customer", ar: "العميل" },
	"address": { en: "Address", ar: "العنوان" },
	"contact": { en: "Contact", ar: "جهة الاتصال" },
	"parcels": { en: "Parcels", ar: "الطرود" },
	"weight": { en: "Total weight", ar: "الوزن الإجمالي" },
	"value": { en: "Value", ar: "القيمة" },
	"pickup.date": { en: "Pickup date", ar: "تاريخ الاستلام" },
	"no.data": { en: "No shipments found", ar: "لا توجد شحنات" },
	"no.assign": { en: "No shipments are assigned to you yet.", ar: "لا توجد شحنات مخصصة لك حتى الآن." },
	"no.delivered": { en: "No delivered shipments yet.", ar: "لا توجد شحنات تم توصيلها بعد." },
	"no.transit": { en: "Nothing is in transit right now.", ar: "لا يوجد شحنات قيد التوصيل حالياً." },
	"no.pending": { en: "Nothing pending. Enjoy your day!", ar: "لا يوجد شحنات معلّقة. يوم سعيد!" },
	"no.failed": { en: "No failed deliveries.", ar: "لا توجد شحنات فاشلة." },
	"back": { en: "Back", ar: "رجوع" },
	"dashboard": { en: "Dashboard", ar: "الرئيسية" },
	"delivery.title": { en: "Complete Delivery", ar: "إتمام التوصيل" },
	"delivery.sub": { en: "Collect signature, photo & location", ar: "اجمع التوقيع والصورة والموقع" },
	"field.status": { en: "Delivery Status", ar: "حالة التوصيل" },
	"status.next": { en: "In Transit", ar: "قيد التوصيل" },
	"field.received": { en: "Received By", ar: "اسم المستلِم" },
	"field.received.ph": { en: "Name of the person receiving", ar: "اسم الشخص المستلِم للشحنة" },
	"field.remark": { en: "Remark", ar: "ملاحظات" },
	"field.remark.ph": { en: "Notes (optional)", ar: "ملاحظات (اختياري)" },
	"req": { en: "required", ar: "مطلوب" },
	"sig.title": { en: "Customer Signature", ar: "توقيع العميل" },
	"sig.hint": { en: "Sign inside the white box", ar: "وقع داخل الصندوق الأبيض" },
	"sig.clear": { en: "Clear", ar: "مسح" },
	"sig.undo": { en: "Undo", ar: "تراجع" },
	"sig.done": { en: "Signature captured", ar: "تم التقاط التوقيع" },
	"sig.empty": { en: "Signature missing", ar: "لا يوجد توقيع" },
	"photo.title": { en: "Proof Photo", ar: "صورة إثبات" },
	"photo.take": { en: "Take Photo", ar: "التقاط صورة" },
	"photo.retake": { en: "Retake", ar: "إعادة التقاط" },
	"photo.empty": { en: "Photograph the delivered shipment", ar: "صور الشحنة بعد التوصيل" },
	"photo.done": { en: "Photo attached", ar: "تم إرفاق الصورة" },
	"loc.title": { en: "Delivery Location", ar: "موقع التوصيل" },
	"loc.capture": { en: "Capture Location", ar: "تحديد الموقع" },
	"loc.recapture": { en: "Recapture", ar: "إعادة التحديد" },
	"loc.done": { en: "Location captured", ar: "تم تحديد الموقع" },
	"loc.looking": { en: "Acquiring GPS signal…", ar: "جارٍ الاتصال بالأقمار الصناعية…" },
	"loc.denied": { en: "Location access denied. Enable GPS and retry.", ar: "تم رفض الوصول للموقع. فعّل تحديد الموقع وحاول مجدداً." },
	"loc.unavailable": { en: "Location unavailable on this device.", ar: "تحديد الموقع غير متاح على هذا الجهاز." },
	"loc.fail": { en: "Could not get your location.", ar: "تعذر تحديد موقعك." },
	"loc.acc": { en: "Accuracy", ar: "الدقة" },
	"loc.secure": { en: "GPS requires a secure (HTTPS) connection.", ar: "تحديد الموقع يتطلب اتصالاً آمناً HTTPS." },
	"submit": { en: "Submit Delivery", ar: "إرسال التوصيل" },
	"submitting": { en: "Submitting…", ar: "جارٍ الإرسال…" },
	"err.signature": { en: "Please capture the customer signature.", ar: "يرجى التقاط توقيع العميل." },
	"err.photo": { en: "Please attach a proof photo.", ar: "يرجى إرفاق صورة إثبات." },
	"err.location": { en: "Please capture the delivery location.", ar: "يرجى تحديد موقع التوصيل." },
	"err.received": { en: "Please enter the name of the receiver.", ar: "يرجى إدخال اسم المستلِم." },
	"err.network": { en: "Connection error. Please try again.", ar: "خطأ في الاتصال. حاول مجدداً." },
	"err.perm": { en: "You don't have permission.", ar: "ليس لديك صلاحية." },
	"err.retry": { en: "Please retry.", ar: "حاول مجدداً." },
	"success.title": { en: "Delivery submitted", ar: "تم إرسال التوصيل" },
	"success.sub": { en: "Proof of delivery has been saved.", ar: "تم حفظ إثبات التوصيل بنجاح." },
	"done": { en: "Done", ar: "تم" },
	"new.delivery": { en: "Back to shipments", ar: "العودة للشحنات" },
	"proof.no": { en: "Reference", ar: "مرجع" },
	"lang.label": { en: "ع", ar: "EN" },
	"lang.name": { en: "العربية", ar: "English" },
	"live.label": { en: "Live", ar: "مباشر" },
	"assigned.you": { en: "Assigned to you", ar: "مخصص لك" },
	"tap.details": { en: "Open delivery", ar: "فتح التوصيل" },
	"log": { en: "Live location is broadcasting", ar: "يتم بث موقعك لحظياً" },
	"tracking": { en: "Driver Tracking", ar: "تتبع السائقين" },
	"tracking.sub": { en: "Updated", ar: "آخر تحديث" },
	"drivers.live": { en: "active drivers", ar: "سائق نشط" },
	"cur.shipment": { en: "Current shipment", ar: "الشحنة الحالية" },
	"last.ping": { en: "Last ping", ar: "آخر ظهور" },
	"just.now": { en: "just now", ar: "الآن" },
	"min.ago": { en: "min ago", ar: "دقيقة" },
	"seconds.ago": { en: "sec ago", ar: "ثانية" },
	"no.drivers": { en: "No driver location data yet.", ar: "لا توجد بيانات لمواقع السائقين بعد." },
	"offline": { en: "offline", ar: "غير متصل" },
	"sign.out": { en: "Sign out", ar: "خروج" },
	"menu": { en: "Menu", ar: "القائمة" },
	"view.pod": { en: "View proof", ar: "عرض الإثبات" },
	"delivered.at": { en: "Delivered", ar: "تم التوصيل" },
	"not.delivered": { en: "Not Delivered", ar: "لم يتم التوصيل" },
	"in.transit": { en: "In Transit", ar: "قيد التوصيل" },
	"partially": { en: "Partially Delivered", ar: "توصيل جزئي" }
};

TD.lang = localStorage.getItem("td_lang") || (navigator.language && navigator.language.toLowerCase().startsWith("ar") ? "ar" : "en");

TD.t = function (key) {
	const entry = TD.keys[key];
	if (!entry) return key;
	return entry[TD.lang] || entry.en;
};

TD.applyLang = function () {
	if (TD.lang === "ar") {
		document.documentElement.lang = "ar";
		document.documentElement.dir = "rtl";
		document.body.classList.add("ar");
	} else {
		document.documentElement.lang = "en";
		document.documentElement.dir = "ltr";
		document.body.classList.remove("ar");
	}
	localStorage.setItem("td_lang", TD.lang);
	document.querySelectorAll("[data-i18n]").forEach(function (el) {
		const txt = TD.t(el.getAttribute("data-i18n"));
		if (el.tagName === "INPUT" || el.tagName === "TEXTAREA") el.setAttribute("placeholder", txt);
		else el.innerHTML = txt;
	});
	document.querySelectorAll("[data-i18n-html]").forEach(function (el) { el.innerHTML = TD.t(el.getAttribute("data-i18n-html")); });
	const toggles = document.querySelectorAll(".lang-toggle");
	toggles.forEach(function (b) { if (b) b.textContent = TD.t("lang.name"); });
};

TD.toggleLang = function () {
	TD.lang = TD.lang === "en" ? "ar" : "en";
	TD.applyLang();
	if (typeof TD.onLangChange === "function") TD.onLangChange(TD.lang);
};

/* ─── API ─────────────────────────────────────────── */
TD.api = function (method, args) {
	return fetch("/api/method/" + method, {
		method: "POST",
		credentials: "same-origin",
		headers: {
			"Content-Type": "application/json",
			"X-Frappe-CSRF-Token": window.TD_CONFIG ? window.TD_CONFIG.csrf_token : ""
		},
		body: JSON.stringify(args || {})
	}).then(function (r) { return r.json(); }).then(function (data) {
		if (data.exc_type) { throw data; }
		return data.message;
	});
};

TD.uploadFile = function (dataURL, filename) {
	const blob = TD.dataURLToBlob(dataURL);
	const fd = new FormData();
	fd.append("file", blob, filename || "upload.png");
	fd.append("is_private", "0");
	fd.append("doctype", "Delivery Proof");
	return fetch("/api/method/upload_file", {
		method: "POST",
		credentials: "same-origin",
		headers: { "X-Frappe-CSRF-Token": window.TD_CONFIG ? window.TD_CONFIG.csrf_token : "" },
		body: fd
	}).then(function (r) { return r.json(); }).then(function (data) {
		if (data.exc_type) { throw data; }
		return data.message;
	});
};

TD.dataURLToBlob = function (dataURL) {
	const parts = dataURL.split(",");
	const mime = parts[0].match(/:(.*?);/)[1];
	const b64 = atob(parts[1]);
	const len = b64.length;
	const bytes = new Uint8Array(len);
	for (let i = 0; i < len; i++) bytes[i] = b64.charCodeAt(i);
	return new Blob([bytes], { type: mime });
};

/* ─── Toast ───────────────────────────────────────── */
let toastTimer = null;
TD.toast = function (msg, type) {
	const el = document.getElementById("toast");
	if (!el) return;
	el.textContent = msg;
	el.className = "show " + (type || "");
	clearTimeout(toastTimer);
	toastTimer = setTimeout(function () { el.className = ""; }, 2600);
};

/* ─── Formatting ──────────────────────────────────── */
TD.fmtDateTime = function (iso) {
	if (!iso) return "—";
	const d = new Date(iso.replace(" ", "T"));
	if (isNaN(d)) return iso;
	const opts = { day: "2-digit", month: "short", hour: "2-digit", minute: "2-digit" };
	return d.toLocaleString(TD.lang === "ar" ? "ar" : "en", opts);
};

TD.fmtValue = function (v, cur) {
	if (v === null || v === undefined || v === "") return "—";
	if (TD.lang === "ar") return v.toLocaleString("ar-EG");
	return v.toLocaleString("en-US");
};

TD.esc = function (s) {
	return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
		return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
	});
};

TD.age = function (dt) {
	const secs = Math.max(0, (Date.now() - new Date(dt.replace(" ", "T")).getTime()) / 1000);
	if (secs < 60) return Math.round(secs) + " " + TD.t("seconds.ago");
	if (secs < 3600) return Math.round(secs / 60) + " " + TD.t("min.ago");
	return Math.round(secs / 3600) + "h";
};

document.addEventListener("DOMContentLoaded", TD.applyLang);