const lcidDictionary = {
    "Afrikaans": "af", "Albanian": "sq", "Amharic": "am", "Arabic - Algeria": "ar-dz",
    "Arabic - Bahrain": "ar-bh", "Arabic - Egypt": "ar-eg", "Arabic - Iraq": "ar-iq",
    "Arabic - Jordan": "ar-jo", "Arabic - Kuwait": "ar-kw", "Arabic - Lebanon": "ar-lb",
    "Arabic - Libya": "ar-ly", "Arabic - Morocco": "ar-ma", "Arabic - Oman": "ar-om",
    "Arabic - Qatar": "ar-qa", "Arabic - Saudi Arabia": "ar-sa", "Arabic - Syria": "ar-sy",
    "Arabic - Tunisia": "ar-tn", "Arabic - United Arab Emirates": "ar-ae", "Arabic - Yemen": "ar-ye",
    "Armenian": "hy", "Assamese": "as", "Azeri - Cyrillic": "az-az", "Azeri - Latin": "az-az",
    "Basque": "eu", "Belarusian": "be", "Bengali - Bangladesh": "bn", "Bengali - India": "bn",
    "Bosnian": "bs", "Bulgarian": "bg", "Burmese": "my", "Catalan": "ca", "Chinese - China": "zh-cn",
    "Chinese - Hong Kong SAR": "zh-hk", "Chinese - Macau SAR": "zh-mo", "Chinese - Singapore": "zh-sg",
    "Chinese - Taiwan": "zh-tw", "Croatian": "hr", "Czech": "cs", "Danish": "da", "Divehi": "dv",
    "Dutch - Belgium": "nl-be", "Dutch - Netherlands": "nl-nl", "English - Australia": "en-au",
    "English - Belize": "en-bz", "English - Canada": "en-ca", "English - Caribbean": "en-cb",
    "English - Great Britain": "en-gb", "English - India": "en-in", "English - Ireland": "en-ie",
    "English - Jamaica": "en-jm", "English - New Zealand": "en-nz", "English - Philippines": "en-ph",
    "English - Southern Africa": "en-za", "English - Trinidad": "en-tt", "English - United States": "en-us",
    "Estonian": "et", "FYRO Macedonia": "mk", "Faroese": "fo", "Farsi - Persian": "fa", "Filipino": "en",
    "Finnish": "fi", "French - Belgium": "fr-be", "French - Canada": "fr-ca", "French": "fr",
    "French - Luxembourg": "fr-lu", "French - Switzerland": "fr-ch", "Frisian - Netherlands": "fy",
    "Gaelic - Ireland": "gd-ie", "Gaelic - Scotland": "gd", "Galician": "gl", "Georgian": "ka",
    "German - Austria": "de-at", "German - Germany": "de-de", "German - Liechtenstein": "de-li",
    "German - Luxembourg": "de-lu", "German - Switzerland": "de-ch", "Greek": "el", "Guarani - Paraguay": "gn",
    "Gujarati": "gu", "Hebrew": "he", "Hindi": "hi", "Hungarian": "hu", "Icelandic": "is", "Igbo - Nigeria": "en",
    "Indonesian": "id", "Italian - Italy": "it-it", "Italian - Switzerland": "it-ch", "Japanese": "ja",
    "Kannada": "kn", "Kashmiri": "ks", "Kazakh": "kk", "Khmer": "km", "Konkani": "en", "Korean": "ko",
    "Kyrgyz - Cyrillic": "kk", "Lao": "lo", "Latin": "la", "Latvian": "lv", "Lithuanian": "lt",
    "Malay - Brunei": "ms-bn", "Malay - Malaysia": "ms-my", "Malayalam": "ml", "Maltese": "mt",
    "Manipuri": "en", "Maori": "mi", "Marathi": "mr", "Mongolian": "mn", "Nepali": "ne",
    "Norwegian - Bokml": "nb", "Norwegian - Nynorsk": "nn", "Oriya": "or", "Polish": "pl",
    "Portuguese - Brazil": "pt-br", "Portuguese - Portugal": "pt-pt", "Punjabi": "pa", "Raeto-Romance": "rm",
    "Romanian - Moldova": "ro-mo", "Romanian - Romania": "ro", "Russian": "ru", "Sami Lappish": "se",
    "Sanskrit": "sa", "Serbian - Cyrillic": "sr-sp", "Serbian - Latin": "sr-sp", "Sesotho (Sutu)": "st",
    "Setsuana": "tn", "Sindhi": "sd", "Sinhala": "si", "Slovak": "sk", "Slovenian": "sl", "Somali": "so",
    "Sorbian": "sb", "Spanish - Argentina": "es-ar", "Spanish - Bolivia": "es-bo", "Spanish - Chile": "es-cl",
    "Spanish - Colombia": "es-co", "Spanish - Costa Rica": "es-cr", "Spanish - Dominican Republic": "es-do",
    "Spanish - Ecuador": "es-ec", "Spanish - El Salvador": "es-sv", "Spanish - Guatemala": "es-gt",
    "Spanish - Honduras": "es-hn", "Spanish - Mexico": "es-mx", "Spanish - Nicaragua": "es-ni",
    "Spanish - Panama": "es-pa", "Spanish - Paraguay": "es-py", "Spanish - Peru": "es-pe",
    "Spanish - Puerto Rico": "es-pr", "Spanish - Spain (Traditional)": "es-es", "Spanish - Uruguay": "es-uy",
    "Spanish - Venezuela": "es-ve", "Swahili": "sw", "Swedish - Finland": "sv-fi", "Swedish - Sweden": "sv-se",
    "Syriac": "en", "Tajik": "tg", "Tamil": "ta", "Tatar": "tt", "Telugu": "te", "Thai": "th",
    "Tibetan": "bo", "Tsonga": "ts", "Turkish": "tr", "Turkmen": "tk", "Ukrainian": "uk", "Unicode": "en",
    "Urdu": "ur", "Uzbek - Cyrillic": "uz-uz", "Uzbek - Latin": "uz-uz", "Venda": "en", "Vietnamese": "vi",
    "Welsh": "cy", "Xhosa": "xh", "Yiddish": "yi", "Zulu": "zu"
};

const Spoken = document.getElementById('LanguageSpoken');
const Translate = document.getElementById('LanguageTranslate');


Object.keys(lcidDictionary).forEach((key) => {
    const language = lcidDictionary[key];
    const option = document.createElement("option");
    option.value = language;
    option.text = key;
    Spoken.appendChild(option);
    const clone = option.cloneNode(true);
    Translate.appendChild(clone);
});

// document.appendChild(Spoken);
// document.appendChild(Translate);