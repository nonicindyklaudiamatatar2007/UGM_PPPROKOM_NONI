from PIL import Image, ImageDraw, ImageFont

# -----------------------------
# CANVAS
# -----------------------------
width, height = 1240, 1754  # A4 ratio in pixels
img = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(img)

# -----------------------------
# FONTS (Use default if arial.ttf not available)
# -----------------------------
try:
    title_font = ImageFont.truetype("arial.ttf", 48)
    section_font = ImageFont.truetype("arial.ttf", 36)
    text_font = ImageFont.truetype("arial.ttf", 28)
except OSError:
    title_font = ImageFont.load_default()
    section_font = ImageFont.load_default()
    text_font = ImageFont.load_default()

# -----------------------------
# TITLE
# -----------------------------
draw.text((70, 70), "CURRICULUM VITAE", font=title_font, fill="black")
draw.text((70, 140), "Noni Cindy Klaudia Matatar", font=section_font, fill="black")

# -----------------------------
# SECTION: DATA DIRI
# -----------------------------
y = 240
draw.text((70, y), "I. DATA DIRI", font=section_font, fill="black")
y += 60
data = [
    "Nama : Noni Cindy Klaudia Matatar",
    "Asal : Papua",
    "Alamat Domisili : Yogyakarta",
    "Telepon : 08xxxxxxxx",
    "Email : noni.xx @gmail.com",
    "Universitas : Universitas Gadjah Mada",
    "Fakultas/Prodi : Sekolah Vokasi – Teknologi Rekayasa Internet",
    "Angkatan : 2024",
]
for d in data:
    draw.text((90, y), d, font=text_font, fill="black")
    y += 40

# -----------------------------
# SECTION: PENGALAMAN ORGANISASI
# -----------------------------
y += 40
draw.text((70, y), "II. PENGALAMAN ORGANISASI", font=section_font, fill="black")
y += 60

org = [
    "KEMPGAMA UGM – Divisi Humas Publikasi (2024–sekarang)",
    "- Mengelola dan mengedit konten visual untuk publikasi.",
    "- Membuat materi untuk media sosial dan dokumentasi.",
    "",
    "GBI Keluarga Allah Yogyakarta – Multimedia (2024–sekarang)",
    "- Bertugas sebagai Media Presentation dan tampilan visual ibadah.",
    "- Menyusun materi visual dan memastikan kelancaran multimedia.",
    "",
    "Joy Fellowship Indonesia – Digital Communication (2024–sekarang)",
    "- Mengelola akun sosial media komunitas.",
    "- Mendesain konten dan copywriting singkat.",
    "",
    "PKL – Nabire Net (Agustus–November 2023)",
    "- Reporter lapangan & penulis berita.",
    "- Melakukan wawancara, membuat berita, dan editing materi berita.",
]
for o in org:
    draw.text((90, y), o, font=text_font, fill="black")
    y += 40

# -----------------------------
# SECTION: KEAHLIAN
# -----------------------------
y += 20
draw.text((70, y), "III. KEAHLIAN", font=section_font, fill="black")
y += 60
skills = [
    "- Desain grafis & editing visual (Canva, Lightroom, CapCut).",
    "- Desain konten media sosial.",
    "- Media presentation untuk ibadah.",
    "- Komunikasi dan publikasi.",
    "- Pengelolaan sosial media.",
    "- Manajemen waktu & kerja tim.",
]
for s in skills:
    draw.text((90, y), s, font=text_font, fill="black")
    y += 40

# -----------------------------
# SECTION: MOTIVASI
# -----------------------------
y += 20
draw.text((70, y), "IV. MOTIVASI", font=section_font, fill="black")
y += 60
motivation = (
    "Saya memiliki ketertarikan kuat pada bidang publikasi dan multimedia. "
    "Melalui pengalaman organisasi dan pelayanan, saya ingin berkontribusi secara "
    "profesional dalam UKM, khususnya di bidang dokumentasi, desain, dan komunikasi digital."
)

# Bungkus teks agar tidak keluar area
import textwrap
for line in textwrap.wrap(motivation, width=85):
    draw.text((90, y), line, font=text_font, fill="black")
    y += 40

# -----------------------------
# SAVE OUTPUT
# -----------------------------
img.save("CV_Noni.png")

print("CV berhasil dibuat! File: CV_Noni.png")