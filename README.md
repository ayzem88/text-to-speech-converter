# تحويل النص إلى صوت / Text to Speech Converter

<div dir="rtl">

## نظرة عامة

أداة لتحويل النصوص العربية إلى ملفات صوتية باستخدام OpenAI Text-to-Speech API. يدعم أصوات عالية الجودة للغة العربية.

## المميزات

- 🎙️ **تحويل النص إلى صوت**: تحويل النصوص العربية إلى ملفات صوتية
- 🔊 **أصوات عالية الجودة**: استخدام نموذج TTS-1-HD
- 📝 **دعم الملفات النصية**: قراءة النصوص من الملفات
- 🎨 **أصوات متعددة**: دعم أصوات مختلفة (nova, alloy, echo, fable, onyx, shimmer)

## التثبيت

### المتطلبات

- Python 3.7 أو أحدث
- OpenAI API key

### خطوات التثبيت

1. استنسخ المستودع:
```bash
git clone https://github.com/ayzem88/text-to-speech-converter.git
cd text-to-speech-converter
```

2. قم بتثبيت المتطلبات:
```bash
pip install openai
```

3. قم بتعيين مفتاح API:
```bash
export OPENAI_API_KEY="your-api-key-here"
```

## الاستخدام

1. ضع النص المراد تحويله في ملف `كتاب.txt`
2. قم بتشغيل البرنامج:
```bash
python "نص إلى صوت.py"
```

3. سيتم إنشاء ملف الصوت `speech.mp3`

## هيكل المشروع

```
تحويل النص إلى صوت/
├── نص إلى صوت.py          # البرنامج الرئيسي
├── كتاب.txt               # ملف النص المدخل
└── speech.mp3             # ملف الصوت الناتج
```

## الملفات الرئيسية

- **نص إلى صوت.py**: البرنامج الرئيسي لتحويل النص إلى صوت

## ملاحظات مهمة

⚠️ **ملاحظة**: 
- يجب الحصول على مفتاح API من OpenAI
- النص يجب أن يكون في ملف `كتاب.txt`
- ملف الصوت الناتج يُحفظ باسم `speech.mp3`

## التطوير المستقبلي

- [ ] واجهة رسومية (GUI)
- [ ] دعم المزيد من الأصوات
- [ ] معالجة ملفات نصية متعددة
- [ ] خيارات إضافية للصوت

## المساهمة

نرحب بمساهماتكم! يرجى قراءة [CONTRIBUTING.md](CONTRIBUTING.md) للمزيد من التفاصيل.

## الترخيص

هذا المشروع مخصص للاستخدام الأكاديمي والبحثي.

## منهج التطوير

أُعتمد في مشاريعي البرمجية على منهج Vibe Coding؛ أسلوب يتجاوز كتابة كلّ سطر يدوياً، إذ أوجّه نماذج الذكاء الاصطناعي بوصف منطقي وواضح للوظيفة المطلوبة، ثم أُقيّم النتائج وأُدخِل التحسينات.

هذا النهج يعزّز السرعة في إنشاء النماذج الأولية والوِحدات البرمجية، ويمنحني تركيزاً أكبر على التصوّر العام والتصميم بدلاً من التفاصيل الدقيقة.

في هذا المستودع، تجد أدوات ومشاريع بُنيت بهذه المقاربة — يُرحّب بتجربتها والمساهمة فيها.

## المطور

تم تطوير هذا المشروع بواسطة **أيمن الطيّب بن نجي** ([ayzem88](https://github.com/ayzem88))

---

# [English]

<div dir="ltr">

## Overview

A tool for converting Arabic texts to audio files using OpenAI Text-to-Speech API. Supports high-quality voices for Arabic language.

## Features

- 🎙️ **Text to Speech Conversion**: Convert Arabic texts to audio files
- 🔊 **High Quality Voices**: Using TTS-1-HD model
- 📝 **Text File Support**: Read texts from files
- 🎨 **Multiple Voices**: Support for different voices (nova, alloy, echo, fable, onyx, shimmer)

## Installation

### Requirements

- Python 3.7 or later
- OpenAI API key

### Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/ayzem88/text-to-speech-converter.git
cd text-to-speech-converter
```

2. Install requirements:
```bash
pip install openai
```

3. Set API key:
```bash
export OPENAI_API_KEY="your-api-key-here"
```

## Usage

1. Place the text to be converted in `كتاب.txt` file
2. Run the program:
```bash
python "نص إلى صوت.py"
```

3. The audio file `speech.mp3` will be created

## Project Structure

```
text-to-speech-converter/
├── نص إلى صوت.py          # Main program
├── كتاب.txt               # Input text file
└── speech.mp3             # Output audio file
```

## Main Files

- **نص إلى صوت.py**: Main program for text to speech conversion

## Important Notes

⚠️ **Note**: 
- You must obtain an API key from OpenAI
- Text must be in `كتاب.txt` file
- Output audio file is saved as `speech.mp3`

## Future Development

- [ ] Graphical user interface (GUI)
- [ ] Support for more voices
- [ ] Process multiple text files
- [ ] Additional voice options

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## License

This project is intended for academic and research use.

## Development Approach

I adopt the Vibe Coding paradigm in my software projects: rather than writing every line manually, I direct AI models with clear natural-language descriptions of the desired functionality, then evaluate and refine the generated code.

This approach accelerates prototype and module creation, allowing me to focus more on concept and design than on low-level implementation details.

In this repository you'll find tools and projects developed with this mindset — feel free to explore and contribute.

## Developer

Developed by **Ayman Atieb ben NJi** ([ayzem88](https://github.com/ayzem88))

</div>

