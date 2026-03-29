import curses
# ====================== HAUPTMENÜ (mit Kurzerklärung) ======================
MAIN_DATA = [
    {"number": 0, "level": 2, "title": "Naturkonstanten",
     "info": "Zusammenstellung aller wichtigen universellen Konstanten\n"
             "(c, h, G, e, k_B, μ₀, ε₀ usw.) mit exakten Werten und Einheiten."},
    {"number": 1, "level": 2, "title": "Newton'sche Mechanik",
     "info": "Grundlagen der klassischen Mechanik:\n"
             "Newton'sche Axiome, Impuls, Energie, Drehimpuls und Gravitation."},
    {"number": 2, "level": 2, "title": "Analytische Mechanik",
     "info": "Lagrange- und Hamilton-Formalismus, kanonische Gleichungen\n"
             "und Erhaltungssätze in verallgemeinerter Form."},
    {"number": 3, "level": 2, "title": "Elektromagnetismus",
     "info": "Maxwell-Gleichungen, Lorentz-Kraft, elektromagnetische Wellen\n"
             "und Energie-Impuls-Dichte des Feldes."},
    {"number": 4, "level": 2, "title": "Optik",
     "info": "Geometrische und Wellenoptik, Interferenz, Beugung,\n"
             "Polarisation und Fresnel-Gleichungen."},
    {"number": 5, "level": 2, "title": "Quantenmechanik",
     "info": "Schrödinger-Gleichung, Operatoren, Unschärferelation,\n"
             "Wasserstoffatom und Spin."},
    {"number": 6, "level": 2, "title": "Festkörperphysik",
     "info": "Kristallstruktur, Phononen, Bändermodell, Halbleiter\n"
             "und Supraleitung."},
    {"number": 7, "level": 2, "title": "Relativitätstheorie",
     "info": "Spezielle und Allgemeine Relativitätstheorie,\n"
             "Lorentz-Transformation und Schwarzschild-Metrik."},
]
# ====================== DETAIL-INHALT (Newton'sche Mechanik) ======================
SUB_DATA = {
        0: [  # Naturkonstanten
        {
            "level": 3,
            "title": "Mechanik",
            "info": "Mechanische und gravitative Konstanten",
            "content": [
                {"text": "Gravitationskonstante:", "formula": "G = 6.67430(15)×10⁻¹¹ m³ kg⁻¹ s⁻²", "info": "Universelle Gravitationskonstante"},
                {"text": "Erdmasse:", "formula": "M_⊕ = 5.97237(±0.00029)×10²⁴ kg", "info": "Masse der Erde"},
                {"text": "Sonnenmasse:", "formula": "M_☉ = 1.9885(±0.0003)×10³⁰ kg", "info": "Masse der Sonne"}
            ]
        },
        {
            "level": 3,
            "title": "Elektromagnetismus",
            "info": "Elektromagnetische Konstanten",
            "content": [
                {"text": "Elementarladung:", "formula": "e = 1.602176634×10⁻¹⁹ C (exakt)", "info": "Elementarladung des Elektrons"},
                {"text": "Lichtgeschwindigkeit:", "formula": "c = 299792458 m/s (exakt)", "info": "Lichtgeschwindigkeit im Vakuum"},
                {"text": "Elektrische Feldkonstante:", "formula": "ε₀ = 8.8541878128(13)×10⁻¹² F/m", "info": "Permittivität des Vakuums"},
                {"text": "Magnetische Feldkonstante:", "formula": "μ₀ = 1.25663706212(19)×10⁻⁶ H/m", "info": "Permeabilität des Vakuums"},
                {"text": "Coulomb-Konstante:", "formula": "k = 8.987551789×10⁹ N·m²/C²", "info": "Coulomb-Konstante"}
            ]
        },
        {
            "level": 3,
            "title": "Quantenmechanik",
            "info": "Quantenmechanische Konstanten",
            "content": [
                {"text": "Plancksche Konstante:", "formula": "h = 6.62607015×10⁻³⁴ J·s (exakt)", "info": "Plancksches Wirkungsquantum"},
                {"text": "Reduzierte Plancksche Konst.:", "formula": "ħ = 1.054571817…×10⁻³⁴ J·s", "info": "Reduziertes Plancksches Wirkungsquantum"},
                {"text": "Feinstrukturkonstante:", "formula": "α ≈ 7.2973525693(11)×10⁻³", "info": "Feinstrukturkonstante"},
                {"text": "Rydberg-Konstante:", "formula": "R_∞ = 1.0973731568160(21)×10⁷ m⁻¹", "info": "Rydberg-Konstante"},
                {"text": "Bohr-Radius:", "formula": "a₀ = 5.29177210903(80)×10⁻¹¹ m", "info": "Bohr-Radius"}
            ]
        },
        {
            "level": 3,
            "title": "Thermodynamik",
            "info": "Thermodynamische Konstanten",
            "content": [
                {"text": "Avogadro-Konstante:", "formula": "N_A = 6.02214076×10²³ mol⁻¹ (exakt)", "info": "Avogadro-Konstante"},
                {"text": "Boltzmann-Konstante:", "formula": "k_B = 1.380649×10⁻²³ J/K (exakt)", "info": "Boltzmann-Konstante"},
                {"text": "Gaskonstante:", "formula": "R = 8.314462618 J mol⁻¹ K⁻¹", "info": "Universelle Gaskonstante"}
            ]
        }
    ],
    
    
    
    
    
    1: [ # Newton'sche Mechanik
        {"level": 3, "title": "1. Axiome und grundlegende Definitionen",
         "info": "Dieser Abschnitt erklärt die drei Newton'schen Axiome und die grundlegenden kinematischen Größen.",
         "content": [
             {"text": "2. Axiom \"Bewegungsgleichung\":", "formula": "F = m a", "info": "Das zweite Newton'sche Axiom verbindet Kraft, Masse und Beschleunigung."},
             {"text": "3. Axiom \"Actio = Reactio\":", "formula": "F_{12} = -F_{21}", "info": "Kräfte zwischen zwei Körpern sind immer gleich groß und entgegengesetzt gerichtet."},
             {"text": "Geschwindigkeit:", "formula": "v := lim_{h->0} (x(t+h)-x(t)) / h", "info": "Definition der momentanen Geschwindigkeit als Ableitung des Ortes nach der Zeit."},
             {"text": "Beschleunigung:", "formula": "a := lim_{h->0} (v(t+h)-v(t)) / h", "info": "Beschleunigung ist die zeitliche Ableitung der Geschwindigkeit."}
         ]},
        {"level": 3, "title": "2. Erhaltungssätze",
         "info": "Die wichtigsten Erhaltungssätze der klassischen Mechanik.",
         "content": [
             {"text": "Kinetische Energie:", "formula": "T = 1/2 m v²", "info": "Energie der Bewegung."},
             {"text": "Potential:", "formula": "F = -grad V", "info": "Kraft ist der negative Gradient des Potentials."},
             {"text": "Gesamtenergie:", "formula": "E = T + V", "info": "Gesamtenergie ist die Summe aus kinetischer und potenzieller Energie."},
             {"text": "Impuls:", "formula": "p = m v", "info": "Impuls ist Masse mal Geschwindigkeit."},
             {"text": "Drehimpuls:", "formula": "L = r × p", "info": "Drehimpuls bezüglich eines Punktes."},
             {"text": "Drehmoment:", "formula": "M = r × F", "info": "Drehmoment ist der Kreuzprodukt aus Orts- und Kraftvektor."}
         ]},
        {"level": 3, "title": "3. Modellsysteme der Mechanik des Massenpunkts",
         "info": "Wichtige einfache mechanische Systeme.",
         "content": []},
        {"level": 4, "title": "3.1 Harmonischer Oszillator",
         "info": "Der klassische Feder-Masse-Oszillator.",
         "content": [
             {"text": "Potential:", "formula": "V = 1/2 k x²", "info": "Potenzial eines harmonischen Oszillators."},
             {"text": "Ort:", "formula": "x(t) = A sin(ωt + δ)", "info": "Lösung der Bewegungsgleichung."},
             {"text": "Energie:", "formula": "E = 1/2 k x² + 1/2 m v²", "info": "Gesamtenergie bleibt konstant."}
         ]},
        {"level": 4, "title": "3.2 Harmonischer Oszillator mit Stokes-Reibung",
         "info": "Gedämpfter Oszillator.",
         "content": [{"text": "...", "formula": "", "info": ""}]},
        {"level": 4, "title": "3.3 Getriebener harmonischer Oszillator",
         "info": "Oszillator mit äußerer Anregung.",
         "content": [{"text": "...", "formula": "", "info": ""}]},
        {"level": 4, "title": "3.4 Schiefer Wurf",
         "info": "Wurfbewegung unter Schwerkraft.",
         "content": [
             {"text": "Höhe-Weite Zusammenhang:", "formula": "y(x) = -g/(2v0²cos²alpha) x² + tan alpha x", "info": "Bahngleichung des schiefen Wurfs."},
             {"text": "Maximale Höhe des Wurfs:", "formula": "H = v0²/(2g) sin²alpha", "info": "Höhe beim höchsten Punkt."},
             {"text": "Wurfweite:", "formula": "L = 2v0² sin(alpha) cos(alpha)/g", "info": "Reichweite auf ebener Fläche."}
         ]},
        {"level": 4, "title": "3.5 Fadenpendel",
         "info": "Kleinschwingungen eines Pendels.",
         "content": [{"text": "Periodendauer:", "formula": "T = 2pi sqrt(l/g)", "info": "Periode für kleine Auslenkungen."}]},
        {"level": 3, "title": "4. Reale Körper",
         "info": "Mechanik ausgedehnter Körper.",
         "content": []},
        {"level": 4, "title": "4.1 Reibung",
         "info": "Verschiedene Reibungsarten.",
         "content": [
             {"text": "Haftreibung:", "formula": "F_H = mu_H F_N", "info": "Haftreibung verhindert Relativbewegung."},
             {"text": "Gleitreibung:", "formula": "F_G = mu_G F_N", "info": "Reibung bei gleitender Bewegung."},
             {"text": "Rollreibung:", "formula": "M_R = mu_R F_N", "info": "Reibungsmoment beim Rollen."}
         ]},
        {"level": 4, "title": "4.2 Deformation",
         "info": "Elastische und plastische Verformung.",
         "content": [{"text": "...", "formula": "", "info": ""}]},
    ],
    # Hier kannst du später die anderen Kapitel (0, 2, 3 …) genau gleich einfügen
}
# ===================================================================
def init_colors():
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_BLUE, -1) # Pfeile
    curses.init_pair(5, curses.COLOR_RED, -1) # Rote Tasten
    curses.init_pair(6, curses.COLOR_YELLOW, -1) # Orange >>>-Titel

def print_help_main(stdscr, height):
    stdscr.addstr(height - 5, 0, "Eingabe ")
    stdscr.attron(curses.color_pair(5))
    stdscr.addstr(height - 5, 8, "[↑],[↓]")
    stdscr.attroff(curses.color_pair(5))
    stdscr.addstr(height - 5, 16, "zum Navigieren des Cursors")
    stdscr.addstr(height - 4, 0, "Eingabe ")
    stdscr.attron(curses.color_pair(5))
    stdscr.addstr(height - 4, 8, "[ENTER]")
    stdscr.attroff(curses.color_pair(5))
    stdscr.addstr(height - 4, 16, "zum Auswählen des markierten Kapitels")
    stdscr.addstr(height - 3, 0, "Eingabe ")
    stdscr.attron(curses.color_pair(5))
    stdscr.addstr(height - 3, 8, "[i]")
    stdscr.attroff(curses.color_pair(5))
    stdscr.addstr(height - 3, 12, "für mehr Informationen zum markierten Thema")
    stdscr.addstr(height - 2, 0, "Eingabe ")
    stdscr.attron(curses.color_pair(5))
    stdscr.addstr(height - 2, 8, "[0]-[7]")
    stdscr.attroff(curses.color_pair(5))
    stdscr.addstr(height - 2, 16, "zum schnelleren Öffnen des jeweiligen Kapitels")
    stdscr.addstr(height - 1, 0, "Eingabe ")
    stdscr.attron(curses.color_pair(5))
    stdscr.addstr(height - 1, 8, "[q]")
    stdscr.attroff(curses.color_pair(5))
    stdscr.addstr(height - 1, 12, "zum Zurückgehen/Beenden")

def print_help_chapter(stdscr, height):
    stdscr.addstr(height - 5, 0, "Eingabe ")
    stdscr.attron(curses.color_pair(5))
    stdscr.addstr(height - 5, 8, "[↑],[↓]")
    stdscr.attroff(curses.color_pair(5))
    stdscr.addstr(height - 5, 16, "zum Navigieren des Cursors")
    stdscr.addstr(height - 4, 0, "Eingabe ")
    stdscr.attron(curses.color_pair(5))
    stdscr.addstr(height - 4, 8, "[ENTER]")
    stdscr.attroff(curses.color_pair(5))
    stdscr.addstr(height - 4, 16, "zum Auswählen des markierten Kapitels")
    stdscr.addstr(height - 3, 0, "Eingabe ")
    stdscr.attron(curses.color_pair(5))
    stdscr.addstr(height - 3, 8, "[i]")
    stdscr.attroff(curses.color_pair(5))
    stdscr.addstr(height - 3, 12, "für mehr Informationen zum markierten Thema")
    stdscr.addstr(height - 2, 0, "Eingabe ")
    stdscr.attron(curses.color_pair(5))
    stdscr.addstr(height - 2, 8, "[a]")
    stdscr.attroff(curses.color_pair(5))
    stdscr.addstr(height - 2, 12, "zum Ausklappen aller Kapitel")
    stdscr.addstr(height - 1, 0, "Eingabe ")
    stdscr.attron(curses.color_pair(5))
    stdscr.addstr(height - 1, 8, "[q]")
    stdscr.attroff(curses.color_pair(5))
    stdscr.addstr(height - 1, 12, "zum Zurückgehen/Beenden")

def print_help_info(stdscr, height):
    stdscr.attron(curses.color_pair(0))
    stdscr.addstr(height - 2, 0, "Eingabe ")
    stdscr.attron(curses.color_pair(5))
    stdscr.addstr(height - 2, 8, "[i]")
    stdscr.attroff(curses.color_pair(5))
    stdscr.addstr(height - 2, 12, "zum Schließen der Information")
    stdscr.addstr(height - 1, 0, "Eingabe ")
    stdscr.attron(curses.color_pair(5))
    stdscr.addstr(height - 1, 8, "[q]")
    stdscr.attroff(curses.color_pair(5))
    stdscr.addstr(height - 1, 12, "zum Zurückgehen/Beenden")

def show_info(stdscr, title, info_text):
    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        stdscr.attroff(curses.color_pair(1) | curses.A_BOLD)
        stdscr.addstr(0, 1, f"Informationen zu {title}")
        y = 3
        stdscr.attron(curses.color_pair(1))
        for line in info_text.split('\n'):
            if y >= height - 4:
                break
            stdscr.addstr(y, 2, line)
            y += 1
        stdscr.attroff(curses.color_pair(1))
        print_help_info(stdscr, height)
        stdscr.refresh()
        key = stdscr.getch()
        if key in (ord('q'), ord('Q'), ord('i'), ord('I')):
            return

def show_main_menu(stdscr):
    current = 0
    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        stdscr.attron(curses.color_pair(1) | curses.A_BOLD)
        stdscr.addstr(0, 0, ">")
        stdscr.attroff(curses.color_pair(1) | curses.A_BOLD)
        stdscr.addstr(0, 1, " Formelsammlung Physik")
        y = 2
        for i, item in enumerate(MAIN_DATA):
            if y >= height - 7:
                break
            prefix = ">" * item["level"]
            line = f"{prefix} {item['title']}"
            num_str = f" [{item['number']}]"
            if i == current:
                stdscr.attron(curses.A_REVERSE | curses.A_BOLD)
                stdscr.addstr(y, 0, line)
                stdscr.attroff(curses.A_REVERSE | curses.A_BOLD)
                stdscr.attron(curses.A_DIM)
                stdscr.addstr(y, len(line), num_str)
                stdscr.attroff(curses.A_DIM)
            else:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, 0, prefix)
                stdscr.attroff(curses.color_pair(1))
                stdscr.addstr(y, len(prefix), f" {item['title']}")
                stdscr.attron(curses.A_DIM)
                stdscr.addstr(y, len(prefix) + len(f" {item['title']}"), num_str)
                stdscr.attroff(curses.A_DIM)
            y += 1
        print_help_main(stdscr, height)
        stdscr.refresh()
        key = stdscr.getch()
        if key == curses.KEY_UP and current > 0:
            current -= 1
        elif key == curses.KEY_DOWN and current < len(MAIN_DATA) - 1:
            current += 1
        elif key in (curses.KEY_ENTER, 10, 13) or (ord('0') <= key <= ord('7')):
            if ord('0') <= key <= ord('7'):
                num = key - ord('0')
            else:
                num = current
            if num in SUB_DATA and SUB_DATA[num]:
                show_chapter(stdscr, num, MAIN_DATA[num]["title"])
        elif key in (ord('i'), ord('I')):
            item = MAIN_DATA[current]
            show_info(stdscr, item["title"], item["info"])
        elif key in (ord('q'), ord('Q')):
            break

def show_chapter(stdscr, chapter_num, chapter_title):
    data = SUB_DATA.get(chapter_num, [])
    if not data:
        return
    expanded = [False] * len(data)
    current = 0
    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        # Sub-Header (wird immer zuerst gezeichnet → verschwindet nie)
        stdscr.attron(curses.color_pair(1) | curses.A_BOLD)
        stdscr.addstr(0, 0, ">")
        stdscr.attroff(curses.color_pair(1) | curses.A_BOLD)
        stdscr.addstr(0, 1, " Formelsammlung Physik")
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(1, 0, ">>")
        stdscr.attroff(curses.color_pair(1))
        stdscr.addstr(1, 2, f" {chapter_title}")

        # Flat list of all visible rows for perfect cursor navigation
        rows = []
        for i, item in enumerate(data):
            rows.append({"type": "title", "idx": i})
            if expanded[i] and item.get("content"):
                for cline in item["content"]:
                    rows.append({"type": "content", "idx": i, "line": cline})

        y = 3
        for r, row in enumerate(rows):
            if y >= height - 7:
                break
            item = data[row["idx"]]
            if row["type"] == "title":
                prefix = ">" * item["level"]
                title = item["title"]
                title_color = curses.color_pair(6) if item["level"] == 3 else 0
                full_line = f"{prefix} {title}"
                if r == current:
                    stdscr.attron(curses.A_REVERSE | curses.A_BOLD)
                    stdscr.addstr(y, 0, full_line)
                    stdscr.attroff(curses.A_REVERSE | curses.A_BOLD)
                else:
                    stdscr.attron(curses.color_pair(1))
                    stdscr.addstr(y, 0, prefix)
                    stdscr.attroff(curses.color_pair(1))
                    stdscr.attron(title_color)
                    stdscr.addstr(y, len(prefix), f" {title}")
                    stdscr.attroff(title_color)
                y += 1
            else:
                # Formula line - aligned two-column layout
                cline = row["line"]
                left = cline.get("text", "")
                right = cline.get("formula", "")
                # 40 = width of the left column (change if you need more/less space)
                line_text = f"{left:<30}{right}"
                if r == current:
                    stdscr.attron(curses.A_REVERSE | curses.A_BOLD)
                    stdscr.addstr(y, 1, line_text)
                    stdscr.attroff(curses.A_REVERSE | curses.A_BOLD)
                else:
                    stdscr.addstr(y, 1, line_text)
                y += 1 

        # === NEU: Eine Leerzeile nach jedem Formel-Block (wird vom Cursor übersprungen) ===
            if row["type"] == "content" and r + 1 < len(rows) and rows[r+1]["type"] == "title":
                y += 1   # leere Zeile nach dem letzten Formel-Eintrag eines Blocks

        print_help_chapter(stdscr, height)
        stdscr.refresh()
        key = stdscr.getch()
        if key == curses.KEY_UP and current > 0:
            current -= 1
        elif key == curses.KEY_DOWN and current < len(rows) - 1:
            current += 1
        elif key in (curses.KEY_ENTER, 10, 13):
            if rows[current]["type"] == "title":
                idx = rows[current]["idx"]
                expanded[idx] = not expanded[idx]
        elif key in (ord('a'), ord('A')):
            all_open = all(expanded)
            expanded = [not all_open] * len(data)
            current = min(current, len(rows) - 1)
        elif key in (ord('i'), ord('I')):
            row = rows[current]
            item = data[row["idx"]]
            if row["type"] == "title":
                header = item["title"]
                info_text = item.get("info", "Keine weiteren Informationen.")
            else:
                cline = row["line"]
                header = cline["text"]
                info_text = cline.get("info", "Keine weiteren Informationen.")
            show_info(stdscr, header, info_text)
        elif key in (ord('q'), ord('Q')):
            return

def main(stdscr):
    curses.curs_set(0)
    stdscr.keypad(True)
    init_colors()
    show_main_menu(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)
