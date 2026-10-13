import streamlit as st
import os

# Sayfa Ayarları ve Kalp İkonu
st.set_page_config(page_title="Sana Özel Kelime Kartları", page_icon="❤️", layout="centered")

# 🔐 GÜVENLİK VE GİRİŞ KONTROLÜ
DOGRU_KULLANICI = "ecomelo"
DOGRU_SIFRE = "ivandor"

if "giris_yapildi" not in st.session_state:
    st.session_state["giris_yapildi"] = False

if not st.session_state["giris_yapildi"]:
    st.title("🔒 Özel Kelime Kartları")
    st.write("Bu siteye sadece yetkili kişiler erişebilir. Lütfen giriş yap:")
    kullanici_adi = st.text_input("Kullanıcı Adı:")
    sifre = st.text_input("Şifre:", type="password")
    if st.button("Giriş Yap 🚀", use_container_width=True):
        if kullanici_adi == DOGRU_KULLANICI and sifre == DOGRU_SIFRE:
            st.session_state["giris_yapildi"] = True
            st.rerun()
        else:
            st.error("Hatalı kullanıcı adı veya şifre! ❌")
    st.stop()

# ---------------------------------------------------------------------
# 📚 TXT DOSYASINDAN KELİMELERİ OTOMATİK OKUYAN SİSTEM
# ---------------------------------------------------------------------
KELIMELER = []
if os.path.exists("kelimeler.txt"):
    with open("kelimeler.txt", "r", encoding="utf-8") as f:
        for satir in f:
            if " - " in satir:
                ing, tr = satir.strip().split(" - ", 1)
                KELIMELER.append({"ing": ing.strip(), "tr": tr.strip()})

# ⚙️ ARAYÜZ TASARIMI
st.title("🇬🇧 Kelime Öğrenme Kartlarım 🇹🇷")
st.write("Sana özel hazırladığım kelime kartlarına tıklayarak anlamlarını görebilirsin. ✨")

# Çıkış Yap Butonu
col_baslik, col_cikis = st.columns([4, 1])
with col_cikis:
    if st.button("Çıkış Yap 🚪"):
        st.session_state["giris_yapildi"] = False
        st.rerun()

st.divider()
st.subheader(f"📚 Toplam {len(KELIMELER)} Kelime Kartın Var")

# Kart Arama Çubuğu
arama = st.text_input("🔍 Kelime Ara (İngilizce):", placeholder="Aramak istediğin kelimeyi yaz...")

# Kartları Listeleme Alanı
for index, kart in enumerate(KELIMELER):
    if arama.lower() not in kart['ing'].lower():
        continue
        
    with st.expander(f"📦 {kart['ing'].upper()}", expanded=False):
        st.markdown(f"### Anlamı:")
        st.info(f"💡 {kart['tr']}")
        st.write("---")
        st.caption("❤️ *Bu kelimeyi öğrendiysen bir sonraki karta geçebilirsin!*")
