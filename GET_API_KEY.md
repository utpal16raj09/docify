# 🔑 How to Get a Working Gemini API Key

Your current API key appears to be invalid or expired. Here's how to get a fresh, working API key:

## 🚀 Step-by-Step Guide

### 1. Visit Google AI Studio
- Go to: **https://aistudio.google.com/**
- Sign in with your Google account

### 2. Get Your API Key
- Click the **"Get API Key"** button (usually in the top-right)
- Choose **"Create API key in new project"** or select an existing project
- Copy the generated API key immediately (you won't see it again!)

### 3. Update Your .env File
Replace the current key in your `.env` file:

```bash
# Replace this line in .env:
GEMINI_API_KEY=""

# With your new key:
GEMINI_API_KEY=YOUR_NEW_API_KEY_HERE
```

### 4. Test Your New Key
Run the test script to verify it works:

```bash
python test_gemini_api.py
```

## 🆓 Free Tier Limits

Google Gemini offers generous free limits:
- **15 requests per minute**
- **1,500 requests per day**
- **1 million tokens per month**

This is more than enough for testing and development!

## 🔧 Alternative: Use Mock Mode

If you just want to see the premium UI without AI features, the demo will work in mock mode. The backend will simulate API responses for demonstration purposes.

## 🎯 What You Get

With a working API key, your premium demo will have:
- ✅ Real AI-powered code summaries
- ✅ Intelligent documentation generation
- ✅ Smart content analysis
- ✅ Premium Gemini AI integration

## 🆘 Troubleshooting

### Common Issues:

1. **"API key invalid"**
   - Generate a new key at https://aistudio.google.com/
   - Make sure you copied the entire key

2. **"Quota exceeded"**
   - Check your usage at https://aistudio.google.com/
   - Wait for quota reset (daily/monthly)

3. **"Permission denied"**
   - Ensure your Google account has access to Gemini
   - Try creating the key in a new project

### Still Having Issues?

The premium demo will work beautifully even without a real API key - it will use mock responses that demonstrate all the premium features and UI interactions!

## 🎨 Demo Features (With or Without API Key)

Your premium demo includes:
- 🌑 Ultra-dark premium theme
- 💎 Glassmorphism effects
- ✨ 3D animations and transitions
- 🎯 Perfect 3-card pricing layout
- 🚀 Premium particle system
- 💫 Advanced hover effects
- 📱 Responsive design


The UI is fully functional and showcases the premium SaaS experience!
