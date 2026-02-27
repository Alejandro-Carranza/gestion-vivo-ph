import streamlit as st
import base64

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

bg_base64 = get_base64("edificio_vivo.jpg")
logo_base64 = get_base64("logo_vivo.png")

# --- INYECCIÓN DE CSS AVANZADO (UX/UI FUTURISTA + BOTÓN FLOTANTE) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;800&display=swap');

    /* BOTÓN FLOTANTE DORADO PARA EL MENÚ (RESCATE DE SIDEBAR) */
    [data-testid="stSidebarCollapsedControl"] {{
        background-color: #FFD700 !important;
        color: #002366 !important;
        border-radius: 50% !important;
        width: 65px !important;
        height: 65px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        position: fixed !important;
        top: 25px !important;
        left: 25px !important;
        z-index: 999999 !important;
        box-shadow: 0 0 25px rgba(255, 215, 0, 0.7) !important;
        cursor: pointer !important;
    }}
    [data-testid="stSidebarCollapsedControl"] svg {{
        fill: #002366 !important;
        width: 35px !important;
        height: 35px !important;
    }}

    #MainMenu {{visibility: hidden;}}
    header {{visibility: hidden;}}
    footer {{visibility: hidden;}}

    @keyframes pan-bg {{
        0% {{ background-position: 0% 0%; background-size: 100%; }}
        100% {{ background-position: 100% 100%; background-size: 110%; }}
    }}
    
    .stApp {{
        background-image: linear-gradient(135deg, rgba(4, 11, 22, 0.96) 0%, rgba(10, 25, 60, 0.88) 100%), url("data:image/png;base64,{bg_base64}");
        animation: pan-bg 90s infinite alternate cubic-bezier(0.45, 0.05, 0.55, 0.95);
        background-attachment: fixed;
        font-family: 'Montserrat', sans-serif !important;
    }}
    
    h1, h2, h3, p, li, span {{ color: #F0F4F8 !important; font-family: 'Montserrat', sans-serif !important; }}
    
    .legal-card {{
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 215, 0, 0.15);
        border-left: 4px solid #FFD700;
        padding: 30px;
        border-radius: 16px;
        backdrop-filter: blur(12px);
        margin-bottom: 25px;
        transition: all 0.4s ease;
    }}
    .legal-card:hover {{
        transform: translateY(-5px);
        background: rgba(255, 255, 255, 0.06);
        border-color: #FFD700;
    }}

    .highlight-yellow {{ color: #FFD700 !important; font-weight: 800; text-transform: uppercase; font-size: 1.1rem; }}
    .title-glow {{ text-shadow: 0 0 20px rgba(255, 215, 0, 0.4); font-weight: 800; letter-spacing: 2px; }}

    div[role="radiogroup"] > label {{
        background: rgba(4, 11, 22, 0.6) !important;
        border: 1px solid rgba(255, 215, 0, 0.3) !important;
        border-radius: 50px !important;
        padding: 10px 30px !important;
        margin: 5px !important;
        transition: all 0.3s !important;
    }}
    div[role="radiogroup"] > label:hover {{
        box-shadow: 0 0 15px rgba(255, 215, 0, 0.4) !important;
    }}

    .legal-card li {{ font-size: 1.02rem; line-height: 1.5; color: #D1D5DB !important; margin-bottom: 12px; }}
    hr {{ background-image: linear-gradient(to right, rgba(0,0,0,0), rgba(255,215,0,0.5), rgba(0,0,0,0)); }}
    </style>
""", unsafe_allow_html=True)

# --- ENCABEZADO ---
col_logo, col_title = st.columns([1, 5])
with col_logo:
    if logo_base64:
        st.markdown(f'<div style="text-align:center;"><img src="data:image/png;base64,{logo_base64}" width="140"></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div style="border:2px solid #FFD700; border-radius:15px; text-align:center; padding:20px;">VIVO<br>PH</div>', unsafe_allow_html=True)

with col_title:
    st.markdown("<h1 class='title-glow' style='font-size: 2.2rem;'>INFORME DE SEGUIMIENTO - ENTREGA ZONAS COMUNES</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #FFD700 !important;'>Edificio Vivo PH <span style='color:white;'>vs.</span> Constructora Taller 7 S.A.S.</h3>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<h3 style='text-align: center; color: #FFD700 !important;'>PÁNEL DE CONTROL</h3>", unsafe_allow_html=True)
    menu = st.radio("", ["📋 Contexto del Edificio", "⚖️ Marco Legal (Ley 675)", "🚀 Cronología Judicial", "💡 Conclusiones y Recomendaciones"])
    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.caption("🔒 Acceso Seguro - Administración Vivo PH")

# --- SECCIONES ---
if menu == "📋 Contexto del Edificio":
    st.markdown("<h2 class='title-glow'>Información General del Inmueble</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="legal-card">
        <p>El edificio <b style="color: #FFD700;">Vivo PH</b> se encuentra sometido al Régimen de Propiedad Horizontal bajo:</p>
        <ul>
            <li>📝 <b>Escritura Pública:</b> No 3630, Notaría Octava (8) del 14 de diciembre de 2021.</li>
            <li>📑 <b>Folio Matrícula Inmobiliaria:</b> No 50C-2121935.</li>
            <li>🏗️ <b>Licencia de Construcción:</b> No. 11001-3-21-1906 (13 diciembre 2021).</li>
            <li>⚖️ <b>Marco Regulatorio General:</b> Ley 675 de 2001.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif menu == "⚖️ Marco Legal (Ley 675)":
    st.markdown("<h2 class='title-glow'>Fundamentos del Reglamento</h2>", unsafe_allow_html=True)
    col_l, col_r = st.columns(2)
    with col_l:
        st.markdown('<div class="legal-card"><h3 class="highlight-yellow">🏢 Bienes Comunes (Art. 5)</h3><p>Pertenecientes en proindiviso a todos los propietarios. Facilitan la estabilidad y seguridad de los bienes privados.</p></div>', unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=600", use_column_width=True)
    with col_r:
        st.markdown('<div class="legal-card"><h3 class="highlight-yellow">🛡️ Bienes Esenciales (Art. 5)</h3><p>Indispensables para la existencia y seguridad del edificio: cimientos, estructura, fachadas y losas.</p></div>', unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1503387762-592deb58ef4e?w=600", use_column_width=True)

elif menu == "🚀 Cronología Judicial":
    st.markdown("<h2 class='title-glow' style='text-align:center;'>Trazabilidad Legal</h2>", unsafe_allow_html=True)
    año = st.radio("", ["2023", "2024", "2025", "2026"], horizontal=True, label_visibility="collapsed")
    
    if año == "2023":
        st.markdown("""<div class="legal-card"><h3 class="highlight-yellow">HITOS DEL AÑO 2023</h3><ul>
        <li><b>Marzo 31:</b> Taller Siete entrega bienes esenciales y documentación técnica (planos, garantías, licencias).</li>
        <li><b>Marzo/Abril:</b> Decisión de contratar a <b>Terrakota Construcciones</b> para interventoría de recibo.</li>
        <li><b>Diciembre:</b> Asamblea Extraordinaria exige destinar recursos de cuota extraordinaria al contrato con Terrakota.</li>
        </ul></div>""", unsafe_allow_html=True)
    
    elif año == "2024":
        st.markdown("""<div class="legal-card"><h3 class="highlight-yellow">HITOS DEL AÑO 2024</h3><ul>
        <li><b>Marzo:</b> Entrega informe de interventoría a la copropiedad y a la constructora.</li>
        <li><b>Mayo 18:</b> Asamblea extraordinaria socializa informe de interventoría y solicita iniciar gestiones para obras de reparación.</li>
        <li><b>Mayo 31:</b> Mesa de trabajo. Compromiso de respuesta de Taller 7 para el 7 de junio.</li>
        <li><b>Julio 3 y 30:</b> Radicación de Derechos de Petición ante la falta de cumplimiento de compromisos por parte de Taller 7.</li>
        <li><b>Agosto 14:</b> Queja formal ante la SDHT por deficiencias funcionales en zonas comunes.</li>
        <li><b>Octubre 3:</b> Inspección técnica realizada por la SDHT.</li>
        <li><b>Octubre 10:</b> Tutela contra Taller 7. El 15 de octubre responden prometiendo obras en febrero 2025.</li>
        </ul></div>""", unsafe_allow_html=True)

    elif año == "2025":
        st.markdown("""<div class="legal-card"><h3 class="highlight-yellow">HITOS DEL AÑO 2025</h3><ul>
        <li><b>Marzo 17:</b> Solicitud formal a Taller 7 para iniciar obras según compromiso.</li>
        <li><b>Abril 14:</b> Taller 7 propone cubrir parqueadero P1 con copago del 40% ($10.5M).</li>
        <li><b>Junio:</b> Nueva Tutela ante Juzgado 99 por inasistencia a mesas de trabajo.</li>
        <li><b>Julio 3:</b> Rechazo de Propuesta: La Administración y el Consejo decidieron no aceptar la cobertura del parqueadero en el piso 1.</li>            
        <li><b>Julio 25:</b> Informe de patologia del Ing. Jaime Cortés; hallazgos de infiltración.</li>
        <li><b>Agosto 27:</b> SDHT abre <b>investigación administrativa (Auto 1486)</b> calificando hallazgos como AFECTACIÓN GRAVE y GRAVÍSIMA.</li>
        <li><b>Septiembre 29:</b> Taller 7 remite pólizas "Todo Riesgo Contratista" <b>VENCIDAS</b>.</li>
        <li><b>Octubre 22:</b> Solicitud de conciliación en la Procuraduría. Declarada <b>FALLIDA</b> en noviembre por falta de ánimo conciliatorio.</li>
        <li><b>Noviembre 19:</b> Nuevo Derecho de Petición por Póliza de Estabilidad.</li>
        <li><b>Noviembre 27:</b> sesión de conciliación en la Procuraduría entre la copropiedad y Taller 7. JAIME BRAVO – R.L, , comunica que no tienen ánimo conciliatorio dado que cursan proceso de liquidación ante la Superintendencia de Sociedades. Conclusión: la audiencia se declara FALLIDA y AGOTADA la etapa conciliatoria..</li>
        </ul></div>""", unsafe_allow_html=True)

    elif año == "2026":
        st.markdown("""<div class="legal-card"><h3 class="highlight-yellow">HITOS DEL AÑO 2026</h3><ul>
        <li><b>Enero 13:</b> Juzgado admite tutela en curso.</li>
        <li><b>Enero 28:</b> Taller 7 alega que la Garantía Legal no constituye un documento tangible.</li>
        <li><b>Febrero 10:</b> Administración prepara impugnación para exigir respuesta efectiva y de fondo.</li>
        <li><b>Febrero 20:</b> Notificación de la <b>Resolución 33 (SDHT)</b>: Sanción de <b>$9.930.652</b> por daños graves en parqueadero 20 (Inmueble 406).</li>
        </ul></div>""", unsafe_allow_html=True)

elif menu == "💡 Conclusiones y Recomendaciones":
    st.markdown("<h2 class='title-glow'>Plan de Acción Estratégico</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="legal-card"><h3 class="highlight-yellow">1. Análisis Patrimonial Constructora</h3>
    <p>Tras consultas en Catastro, IGAC y Movilidad, <b>Taller 7 no posee bienes a cargo</b>.</p>
    <ul>
        <li>R.L. Jairo Jaramillo: Único bien en La Mesa (Cundinamarca).</li>
        <li>Segunda R.L.: Único apartamento en Bogotá.</li>
    </ul></div>
    <div class="legal-card"><h3 class="highlight-yellow">2. Reparación zonas comunes</h3>
    <p>Se propone reparar las zonas comunes mediante un proceso de licitación privada:</p>
    <ul>
        <li>Diseño de términos de referencia para ingenieros y arquitectos.</li>
        <li>Evaluación de propuestas por el Consejo y Administración.</li>
        <li>Selección de contratista en Asamblea Extraordinaria.</li>
    </ul></div>
    <div class="legal-card"><h3 class="highlight-yellow">3. Financiación con Banco Agrario</h3>
    <p>Requisitos para solicitud de crédito institucional:</p>
    <ul style="column-count: 2;">
        <li>RUT y Rep. Legal completa.</li>
        <li>Estados financieros 2022-2025.</li>
        <li>Declaraciones de renta.</li>
        <li>Relación de contratos y proveedores.</li>
        <li><b>Acta de Asamblea autorizando el crédito expresamente.</b></li>
    </ul></div>
    """, unsafe_allow_html=True)