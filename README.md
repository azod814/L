# Lawliet 🕶️
Android Wireless Control Tool for Kali Linux  
Built for fast, smart, and cable-free workflow.

---

## 🚀 Features
- USB → Wi-Fi ADB auto switch
- Multiple Android device support
- Manual device selection
- Live phone screen mirroring
- Mouse & keyboard control
- Screenshot capture
- Clean & professional CLI interface
- Custom cyber-style banner

---

## 🧠 How It Works (Simple)
1. Connect phone via USB (one time)
2. Enable USB Debugging
3. Lawliet switches ADB to Wi-Fi automatically
4. Remove cable — connection stays active
5. Control phone directly from laptop

> 📌 Phone restart = USB required once again (Android rule)

---

## 🖥️ Requirements
Lawliet uses official Android tools.

### Install dependencies:
```bash
sudo apt update
sudo apt install adb scrcpy python3 -y


git clone https://github.com/USERNAME/Lawliet.git
cd Lawliet

chmod +x Lawliet.py
./Lawliet.py
