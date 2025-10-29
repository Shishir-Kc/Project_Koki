# --------------------------------------------------------------
# Sexual Health Overview PDF generator
# --------------------------------------------------------------
# Requirements:
#   pip install fpdf
# --------------------------------------------------------------

from fpdf import FPDF

# ------------------- Create PDF object ------------------------
pdf = FPDF()
pdf.add_page()

# ------------------- Document Title ---------------------------
pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "Sexual Health Overview", ln=1, align="C")
pdf.ln(10)  # space after title

# ------------------- Helper to add sections -------------------
def add_section(title: str, content: str):
    """Add a bold heading and a paragraph of text."""
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, title, ln=1)          # heading
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 10, content)       # body text
    pdf.ln(5)                             # space after section

# ------------------- Content ---------------------------------
intro = (
    "Sexual health is an important part of overall well‑being. "
    "It encompasses a range of topics, from anatomy and physiology "
    "to safe practices, consent, and emotional aspects of relationships."
)

anatomy = (
    "Human anatomy includes both external and internal reproductive "
    "structures. Understanding the basic anatomy of the penis, vagina, "
    "uterus, ovaries, testes, and associated glands helps individuals "
    "recognize normal function and identify potential health concerns."
)

safe_practices = (
    "Key safe‑sex practices:\n"
    "- Use barrier methods (condoms, dental dams) to reduce the risk of "
    "STIs and unintended pregnancy.\n"
    "- Get regular STI screenings if sexually active.\n"
    "- Discuss contraception options with a healthcare provider.\n"
    "- Limit the number of sexual partners and maintain open communication."
)

consent = (
    "Consent is a clear, enthusiastic, and ongoing agreement to engage "
    "in any sexual activity. Important points:\n"
    "- Consent must be given freely without pressure or coercion.\n"
    "- It can be withdrawn at any time.\n"
    "- Both parties should feel comfortable asking for clarification."
)

myths = (
    "Common myths and facts:\n"
    "- Myth: \"You can tell if someone has an STI by looking.\"\n"
    "  Fact: Many STIs are asymptomatic; testing is essential.\n"
    "- Myth: \"Birth control pills protect against STIs.\"\n"
    "  Fact: They prevent pregnancy but do not prevent infections.\n"
    "- Myth: \"Only women need regular pelvic exams.\"\n"
    "  Fact: Men also benefit from routine health check‑ups."
)

resources = (
    "Helpful resources for reliable information:\n"
    "- Planned Parenthood (www.plannedparenthood.org)\n"
    "- Centers for Disease Control and Prevention – Sexual Health "
    "(www.cdc.gov/sexualhealth)\n"
    "- World Health Organization – Sexual and Reproductive Health "
    "(www.who.int/health-topics/sexual-health)\n"
    "- Local health clinics or university health centers."
)

# ------------------- Build PDF --------------------------------
add_section("Introduction", intro)
add_section("Human Anatomy Basics", anatomy)
add_section("Safe Sex Practices", safe_practices)
add_section("Understanding Consent", consent)
add_section("Common Myths & Facts", myths)
add_section("Resources & Further Reading", resources)

# ------------------- Save PDF ---------------------------------
pdf.output("Sexual_Health_Overview.pdf")
print("✅ PDF generated: Sexual_Health_Overview.pdf")
