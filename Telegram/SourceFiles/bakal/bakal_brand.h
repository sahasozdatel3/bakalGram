// bakalGram Desktop — personal build based on AyuGram Desktop
// (https://github.com/AyuGram/AyuGramDesktop), which is based on
// Telegram Desktop. Licensed under GNU GPL v3, see LICENSE.
//
// Everything that says "who we are" lives here, so renaming or
// re-linking the client is a one-file change.
#pragma once

#include <QtCore/QRegularExpression>
#include <QtCore/QString>

namespace Bakal {

// Short name: window title, tray menu, settings section.
inline QString ShortName() {
	return QStringLiteral("bakalGram");
}

// Full name: about box, intro screen, notifications.
inline QString FullName() {
	return QStringLiteral("bakalGram Desktop");
}

// Our GitHub repository (source code and builds).
inline QString RepoUrl() {
	return QStringLiteral("https://github.com/sahasozdatel3/bakalGram");
}

inline QString ReleasesUrl() {
	return RepoUrl() + QStringLiteral("/releases");
}

// Upstream we are built on, kept for attribution.
inline QString UpstreamName() {
	return QStringLiteral("AyuGram");
}

inline QString UpstreamRepoUrl() {
	return QStringLiteral("https://github.com/AyuGram/AyuGramDesktop");
}

// AyuGram strings that credit its authors or describe their
// official resources. These keep the original name.
inline bool IsAttributionKey(const QString &key) {
	return key == QStringLiteral("ayu_SettingsWatermark")
		|| key == QStringLiteral("ayu_SupporterPopup")
		|| key == QStringLiteral("ayu_OfficialResourcePopup")
		|| key == QStringLiteral("ayu_ExteraChatsAlert");
}

// Swaps AyuGram branding for ours in a UI string. Leaves words that
// merely start with it (like the @AyuGramReleases username) intact.
inline QString Rebrand(QString text) {
	static const auto re = QRegularExpression(
		QStringLiteral("AyuGram(?![A-Za-z0-9_])"));
	return text.replace(re, ShortName());
}

} // namespace Bakal
