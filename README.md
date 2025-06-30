<h1 align="center">📷 Mobile Image Classifier AI</h1>

<p align="center">
  <em>A clean, powerful image classifier built with Python, Streamlit, and TensorFlow — developed for academic and real-world use.</em>
</p>

<p align="center">
  <img src="screenshots/results_view.png" width="60%" alt="Prediction Example">
</p>

---

## 🧠 About the Project

This project is an intelligent image classification system that uses a pretrained **MobileNetV2** deep learning model to identify objects, animals, and scenes in photos.

It was developed as part of a **Second Year AI Engineering** mini-project to demonstrate real-world application of:
- Convolutional Neural Networks (CNNs)
- Transfer Learning
- Streamlit-based Web UI

---

## 🚀 Features

✅ Upload image (JPG, PNG)  
✅ Predicts top 3 most likely categories  
✅ Works offline, no internet needed after setup  
✅ Runs on Windows, Mac, Linux with Python  
✅ Mobile-optimized UI (PWA-style)

---

## 📸 Screenshots

| Upload Interface | Result View |
|------------------|-------------|
| ![Upload](screenshots/upload_ui.png) | ![Result](screenshots/results_view.png) |

---

## 🔧 Installation & Setup

### 1. Clone this Repository
```bash
git clone https://github.com/Mizna1/image-classifier-project.git
cd image-classifier-project
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the App
```bash
streamlit run image_classifier.py
```

---

## 🧪 How It Works

1. Image is resized to 224x224 and preprocessed
2. AI predicts using `MobileNetV2` trained on ImageNet
3. Top 3 predictions are shown with confidence scores

---

## 📁 Project Structure

```
image-classifier-project/
│
├── image_classifier.py     # Main Streamlit App
├── requirements.txt        # Dependencies
├── README.md               # Project Info
└── screenshots/            # UI snapshots for GitHub display
```

---

## 👩‍💻 Developer

**Mizna1**  
*AI Engineering Student*  
📧 *Optional: add email/github/social links*

---

## 📜 License

This project is licensed under the **MIT License**.  
You are free to use, modify, and share with credit.

---

## 🙌 Acknowledgements

- [TensorFlow](https://www.tensorflow.org/)
- [Keras Applications](https://keras.io/api/applications/)
- [Streamlit](https://streamlit.io/)
- [ImageNet Dataset](https://www.image-net.org/)
