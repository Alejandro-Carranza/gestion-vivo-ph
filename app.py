import streamlit as st
import base64
import os

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Gestión Vivo PH", layout="wide", initial_sidebar_state="expanded")

# --- FUNCIONES DE IMÁGENES Y FONDOS ---
def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        return ""

# Cargar imagen de fondo
bg_base64 = get_base64("edificio_vivo.jpg")
logo_base64 = get_base64("logo_vivo.png")

# Efecto de Movimiento Lento (Ken Burns effect) y Estilos Generales
st.markdown(f"""
    <style>
    /* Ocultar elementos por defecto de Streamlit para aspecto de App Web */
    #MainMenu {{visibility: hidden;}}
    header {{visibility: hidden;}}
    
    /* Animación del fondo */
    @keyframes pan-bg {{
        0% {{ background-position: 0% 0%; background-size: 100%; }}
        50% {{ background-position: 100% 100%; background-size: 105%; }}
        100% {{ background-position: 0% 0%; background-size: 100%; }}
    }}
    
    .stApp {{
        background-image: linear-gradient(rgba(0, 25, 65, 0.9), rgba(0, 15, 45, 0.95)), url("data:image/png;base64,{bg_base64}");
        animation: pan-bg 60s infinite alternate ease-in-out;
        background-attachment: fixed;
    }}
    
    h1, h2, h3, p, li {{ color: #FFFFFF !important; font-family: 'Segoe UI', sans-serif; }}
    
    /* Tarjetas Legales */
    .legal-card {{
        background: rgba(255, 255, 255, 0.05);
        border-left: 5px solid #FFD700;
        padding: 25px;
        border-radius: 8px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        backdrop-filter: blur(5px);
        margin-bottom: 20px;
        height: 100%;
    }}
    .highlight-yellow {{ color: #FFD700 !important; font-weight: bold; }}
    
    /* Selector de Año Estilo Arquitectónico */
    div[role="radiogroup"] > label {{
        background: rgba(0, 35, 102, 0.8) !important;
        border: 2px solid #FFD700 !important;
        border-radius: 10px !important;
        padding: 10px 30px !important;
        margin: 0 10px !important;
        transition: transform 0.3s, background 0.3s !important;
    }}
    div[role="radiogroup"] > label:hover {{
        transform: translateY(-5px) !important;
        background: rgba(255, 215, 0, 0.2) !important;
    }}
    div[data-testid="stMarkdownContainer"] p {{ font-size: 1.1rem; }}
    </style>
""", unsafe_allow_html=True)

# --- ENCABEZADO SUPERIOR IZQUIERDO ---
col_logo, col_title = st.columns([1, 4])
with col_logo:
    if logo_base64:
        st.markdown(f"<img src='data:image/png;base64,{logo_base64}' width='150' style='border-radius: 10px;'>", unsafe_allow_html=True)
    else:
        # Fallback si no está la imagen (Logo Geométrico Creado en CSS)
        st.markdown("""
        <div style="border: 3px solid #FFD700; width: 120px; height: 120px; display: flex; align-items: center; justify-content: center; background: rgba(0,0,0,0.5); border-radius: 15px;">
            <h2 style="color: #FFD700 !important; margin:0; font-size: 28px;">VIVO<br><span style="color: white; font-size: 18px;">PH</span></h2>
        </div>
        """, unsafe_allow_html=True)

with col_title:
    st.markdown("<h1 style='color: #FFD700 !important; margin-bottom: 0;'>INFORME DE GESTIÓN ADMINISTRATIVA</h1>", unsafe_allow_html=True)
    st.markdown("<h3>Conjunto Residencial Vivo PH vs. Constructora Taller 7 S.A.S.</h3>", unsafe_allow_html=True)

st.markdown("<hr style='border-color: rgba(255, 215, 0, 0.5);'>", unsafe_allow_html=True)

# --- MENU LATERAL ---
menu = st.sidebar.radio("Navegación del Informe:", ["📋 Contexto del Edificio", "⚖️ Marco Legal (Ley 675)", "🏗️ Cronología de Gestión Judicial"])
st.sidebar.markdown("---")
st.sidebar.caption("Generado para la Asamblea de Copropietarios - 2026")

# ==========================================
# SECCIÓN 1: CONTEXTO DEL EDIFICIO
# ==========================================
if menu == "📋 Contexto del Edificio":
    st.markdown("<h2 class='highlight-yellow'>Datos Generales del Inmueble</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="legal-card" style="font-size: 1.2rem;">
        <p>El edificio <b>Vivo PH</b>, se encuentra sometido al Régimen de Propiedad Horizontal por medio de:</p>
        <ul>
            <li><b>Escritura Pública:</b> No 3630, Notaría Octava (8) del 14 de diciembre de 2021 (Reglamento de PH).</li>
            <li><b>Folio Matrícula Inmobiliaria:</b> No 50C-2121935.</li>
            <li><b>Licencia de Construcción:</b> No. 11001-3-21-1906 (13 diciembre 2021).</li>
            <li><b>Marco Regulatorio General:</b> Ley 675 de 2001.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# SECCIÓN 2: MARCO LEGAL (CON IMÁGENES)
# ==========================================
elif menu == "⚖️ Marco Legal (Ley 675)":
    st.markdown("<h2 class='highlight-yellow'>Fundamentos del Reglamento de Propiedad Horizontal</h2>", unsafe_allow_html=True)
    
    col_izq, col_der = st.columns(2)
    
    with col_izq:
        st.markdown("""
        <div class="legal-card">
            <h3 class="highlight-yellow">🏢 BIENES COMUNES (Art. 5)</h3>
            <p>Partes del edificio sometido al régimen de propiedad horizontal, pertenecientes en proindiviso a todos los propietarios de bienes privados.</p>
            <p>Facilitan la existencia, estabilidad, funcionamiento, conservación, seguridad, uso, goce o explotación de los bienes de dominio particular.</p>
        </div>
        """, unsafe_allow_html=True)
        # Imagen de referencia Genérica (Puedes cambiar la URL por local ej: st.image("comunes.jpg"))
        st.image("https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?auto=format&fit=crop&w=600&q=80", caption="Referencia: Áreas de circulación y amenidades.")

    with col_der:
        st.markdown("""
        <div class="legal-card">
            <h3 class="highlight-yellow">🛡️ BIENES ESENCIALES (Art. 5)</h3>
            <p>Bienes indispensables para la existencia, estabilidad, conservación y seguridad del edificio, así como los imprescindibles para el uso y disfrute.</p>
            <p><b>Se reputan como esenciales:</b> El terreno, cimientos, estructura, instalaciones generales de servicios, fachadas y los techos o losas de cubierta.</p>
        </div>
        """, unsafe_allow_html=True)
        # Imagen de referencia Genérica
        st.image("https://images.unsplash.com/photo-1503387762-592deb58ef4e?auto=format&fit=crop&w=600&q=80", caption="Referencia: Estructura, cimientos y fachadas.")

# ==========================================
# SECCIÓN 3: CRONOLOGÍA (NUEVO SELECTOR)
# ==========================================
elif menu == "🏗️ Cronología de Gestión Judicial":
    st.markdown("<h2 class='highlight-yellow'>Trazabilidad del Proceso vs. Taller 7</h2>", unsafe_allow_html=True)
    
    # Selector Estilizado
    st.markdown("<p style='text-align: center; color: #FFD700; font-size: 18px;'><b>Seleccione el bloque anual para ver los hitos:</b></p>", unsafe_allow_html=True)
    año = st.radio("", ["2023", "2024", "2025", "2026"], horizontal=True)
    
    st.markdown("<br>", unsafe_allow_html=True)

    if año == "2023":
        st.markdown("""
        <div class="legal-card">
            <h3 class="highlight-yellow">📅 Hitos del Año 2023: Entregas y Auditorías</h3>
            <ul>
                <li><b>Marzo 31:</b> En Asamblea General, Taller 7 entregó a los copropietarios los bienes comunes esenciales y documentación (planos, licencias, garantías).</li>
                <li><b>Marzo/Abril:</b> La Asamblea Extraordinaria aprueba contratar a <b>Terrakota Construcciones</b> para la consultoría de recibo de zonas comunes.</li>
                <li><b>Diciembre:</b> Asamblea exige a la administración destinar recursos de la cuota extraordinaria al contrato con Terrakota, al haberse usado sin autorización previa.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    elif año == "2024":
        st.markdown("""
        <div class="legal-card">
            <h3 class="highlight-yellow">📅 Hitos del Año 2024: Hallazgos y Primeras Acciones</h3>
            <ul>
                <li><b>Marzo:</b> Terrakota entrega informe de interventoría (9 anexos documentando no conformidades). El 29 de marzo se remite a Taller 7.</li>
                <li><b>Mayo 18:</b> Asamblea socializa el informe. Ante el silencio de la constructora, se ordena exigir la reparación inmediata.</li>
                <li><b>Julio 3 y 30:</b> Radicación de Derechos de Petición exigiendo respuesta a los compromisos de la mesa de trabajo de mayo.</li>
                <li><b>Agosto 14:</b> Queja radicada ante la Secretaría Distrital del Hábitat (SDHT) por deficiencias funcionales. Inspección realizada el 3 de octubre.</li>
                <li><b>Octubre 10:</b> Radicación de <b>Tutela</b> en Juzgado 100 por falta de respuesta.</li>
                <li><b>Octubre 15:</b> Taller 7 responde con cronograma, prometiendo obras para febrero de 2025.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    elif año == "2025":
        st.markdown("""
        <div class="legal-card">
            <h3 class="highlight-yellow">📅 Hitos del Año 2025: Sanciones y Lucha por la Garantía</h3>
            <ul>
                <li><b>Abril 14:</b> Taller 7 propone cubrir parqueadero Piso 1, pidiendo a la copropiedad asumir el 40% ($10.5M). <b>Propuesta rechazada en Julio</b> por impacto estructural y legal.</li>
                <li><b>Julio 14:</b> SDHT emite Auto abriendo <b>investigación administrativa</b> contra Taller 7. En agosto (Auto 1486) se califica la situación como <b>AFECTACIÓN GRAVE y GRAVÍSIMA</b>.</li>
                <li><b>Septiembre:</b> Se radica nueva solicitud ante SDHT y nuevo Derecho de Petición pidiendo la Garantía Legal y Pólizas.</li>
                <li><b>Septiembre 27:</b> Tutela (Juzgado 67) por falta de respuesta. Taller 7 remite pólizas <b>VENCIDAS</b> de Aseguradora Solidaria.</li>
                <li><b>Noviembre 27:</b> Conciliación en Procuraduría <b>FALLIDA</b>; Taller 7 argumenta estar en proceso de liquidación ante Supersociedades.</li>
                <li><b>Diciembre 19:</b> Nueva Tutela en el Juzgado 10 Civil Municipal exigiendo la Póliza de Estabilidad de Obra.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    elif año == "2026":
        st.markdown("""
        <div class="legal-card">
            <h3 class="highlight-yellow">📅 Hitos del Año 2026: Acciones en Curso</h3>
            <ul>
                <li><b>Enero 13:</b> Juzgado 13 admite la Tutela, a pesar de los alegatos de la constructora.</li>
                <li><b>Enero 26:</b> El Juez ordena a Taller 7 emitir respuesta de fondo, clara y congruente, sobre la Garantía Legal.</li>
                <li><b>Enero 28 (Respuesta de Taller 7):</b> La constructora argumenta que la Garantía Legal (Art. 8 Ley 1480) <i>"no constituye per se un documento legal y tangible"</i> y que no están obligados a constituir una garantía real.</li>
                <li><b>Febrero 10:</b> La administración prepara documento para <b>impugnar la tutela</b> en caso de que el Juez considere esta respuesta como suficiente o efectiva.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)