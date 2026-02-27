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

# --- INYECCIÓN DE CSS AVANZADO (UX/UI FUTURISTA) ---
st.markdown(f"""
    <style>
    /* 1. Importar Fuente Moderna */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;800&display=swap');

    /* Ocultar elementos nativos de Streamlit */
    #MainMenu {{visibility: hidden;}}
    header {{visibility: hidden;}}
    footer {{visibility: hidden;}}

    /* 2. Fondo Dinámico Mejorado (Dark UI) */
    @keyframes pan-bg {{
        0% {{ background-position: 0% 0%; background-size: 100%; }}
        100% {{ background-position: 100% 100%; background-size: 110%; }}
    }}
    
    .stApp {{
        background-image: linear-gradient(135deg, rgba(4, 11, 22, 0.95) 0%, rgba(10, 25, 60, 0.85) 100%), url("data:image/png;base64,{bg_base64}");
        animation: pan-bg 90s infinite alternate cubic-bezier(0.45, 0.05, 0.55, 0.95);
        background-attachment: fixed;
        font-family: 'Montserrat', sans-serif !important;
    }}
    
    /* Tipografía General */
    h1, h2, h3, p, li, span {{ color: #F0F4F8 !important; font-family: 'Montserrat', sans-serif !important; }}
    
    /* 3. Glassmorphism Cards (Tarjetas de Cristal) */
    .legal-card {{
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 215, 0, 0.15);
        border-left: 4px solid #FFD700;
        padding: 30px;
        border-radius: 16px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        margin-bottom: 25px;
        height: 100%;
        transition: all 0.4s ease;
    }}
    
    /* Micro-interacción: Glow y Lift al pasar el mouse */
    .legal-card:hover {{
        transform: translateY(-5px);
        background: rgba(255, 255, 255, 0.06);
        border: 1px solid rgba(255, 215, 0, 0.5);
        box-shadow: 0 15px 45px 0 rgba(255, 215, 0, 0.15);
    }}

    .highlight-yellow {{ 
        color: #FFD700 !important; 
        font-weight: 800; 
        letter-spacing: 1px; 
        text-transform: uppercase;
        font-size: 1.1rem;
    }}
    
    .title-glow {{
        color: #FFFFFF !important;
        text-shadow: 0 0 20px rgba(255, 215, 0, 0.4);
        font-weight: 800;
        letter-spacing: 2px;
    }}

    /* 4. Selector de Año Neumórfico / Futurista */
    div[role="radiogroup"] {{
        display: flex;
        justify-content: center;
        gap: 15px;
        flex-wrap: wrap;
    }}
    
    div[role="radiogroup"] > label {{
        background: rgba(4, 11, 22, 0.6) !important;
        border: 1px solid rgba(255, 215, 0, 0.3) !important;
        border-radius: 50px !important; 
        padding: 12px 35px !important;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
        backdrop-filter: blur(5px);
    }}
    
    div[role="radiogroup"] > label:hover {{
        background: rgba(255, 215, 0, 0.1) !important;
        border-color: #FFD700 !important;
        box-shadow: 0 0 15px rgba(255, 215, 0, 0.4) !important;
        transform: scale(1.05) !important;
    }}

    /* Estilos de textos en tarjetas */
    .legal-card p, .legal-card li {{
        font-size: 1.05rem;
        line-height: 1.6;
        color: #D1D5DB !important;
        margin-bottom: 8px;
    }}
    
    hr {{
        border: 0;
        height: 1px;
        background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(255, 215, 0, 0.75), rgba(0, 0, 0, 0));
        margin: 30px 0;
    }}
    </style>
""", unsafe_allow_html=True)

# --- ENCABEZADO SUPERIOR IZQUIERDO ---
col_logo, col_title = st.columns([1, 5])
with col_logo:
    if logo_base64:
        st.markdown(f"""
        <div style="background: rgba(255,255,255,0.05); padding: 15px; border-radius: 20px; backdrop-filter: blur(10px); border: 1px solid rgba(255,215,0,0.2); display: inline-block; box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);">
            <img src='data:image/png;base64,{logo_base64}' width='140' style='border-radius: 10px;'>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="border: 2px solid rgba(255, 215, 0, 0.8); width: 140px; height: 140px; display: flex; align-items: center; justify-content: center; background: linear-gradient(135deg, rgba(0,0,0,0.8), rgba(20,20,40,0.9)); border-radius: 20px; box-shadow: 0 0 20px rgba(255,215,0,0.2);">
            <h2 style="color: #FFD700 !important; margin:0; font-size: 32px; font-weight: 800;">VIVO<br><span style="color: #FFF; font-size: 20px; font-weight: 300;">PH</span></h2>
        </div>
        """, unsafe_allow_html=True)

with col_title:
    st.markdown("<h1 class='title-glow' style='margin-bottom: 5px; text-transform: uppercase;'>INFORME DE SEGUIMIENTO - ENTREGA ZONAS COMUNES</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #FFD700 !important; font-weight: 400; letter-spacing: 1px;'>Conjunto Residencial Vivo PH <span style='color: white;'>vs.</span> Constructora Taller 7 S.A.S.</h3>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- MENU LATERAL (SIDEBAR) ---
with st.sidebar:
    st.markdown("<h3 style='text-align: center; color: #FFD700 !important; margin-bottom: 30px;'>PÁNEL DE CONTROL</h3>", unsafe_allow_html=True)
    menu = st.radio("", [
        "📋 Contexto del Edificio", 
        "⚖️ Marco Legal (Ley 675)", 
        "🚀 Cronología Judicial", 
        "💡 Conclusiones y Recomendaciones"
    ])
    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.caption("🔒 Acceso Seguro - Generado para la Asamblea de Copropietarios 2026")

# ==========================================
# SECCIÓN 1: CONTEXTO DEL EDIFICIO
# ==========================================
if menu == "📋 Contexto del Edificio":
    st.markdown("<h2 class='title-glow'>Información General del Inmueble</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="legal-card">
        <p style="font-size: 1.2rem; color: #FFF !important; margin-bottom: 20px;">El edificio <b style="color: #FFD700;">Vivo PH</b> se encuentra legalmente constituido y sometido al Régimen de Propiedad Horizontal bajo los siguientes parámetros:</p>
        <ul style="font-size: 1.15rem; gap: 10px; display: flex; flex-direction: column;">
            <li>📝 <b style="color: #FFF;">Escritura Pública:</b> No 3630, Notaría Octava (8) del 14 de diciembre de 2021.</li>
            <li>📑 <b style="color: #FFF;">Folio Matrícula Inmobiliaria:</b> No 50C-2121935.</li>
            <li>🏗️ <b style="color: #FFF;">Licencia de Construcción:</b> No. 11001-3-21-1906 (13 diciembre 2021).</li>
            <li>⚖️ <b style="color: #FFF;">Marco Regulatorio General:</b> Ley 675 de 2001.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# SECCIÓN 2: MARCO LEGAL
# ==========================================
elif menu == "⚖️ Marco Legal (Ley 675)":
    st.markdown("<h2 class='title-glow'>Fundamentos del Reglamento (Ley 675)</h2>", unsafe_allow_html=True)
    col_izq, col_der = st.columns(2)
    with col_izq:
        st.markdown("""
        <div class="legal-card">
            <h3 class="highlight-yellow">🏢 Bienes Comunes (Art. 5)</h3>
            <p>Partes del edificio sometido al régimen de propiedad horizontal, pertenecientes en proindiviso a todos los propietarios de bienes privados.</p>
            <p>Facilitan la existencia, estabilidad, funcionamiento, conservación, seguridad, uso, goce o explotación de los bienes de dominio particular.</p>
        </div>
        """, unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?auto=format&fit=crop&w=600&q=80", use_column_width=True)

    with col_der:
        st.markdown("""
        <div class="legal-card">
            <h3 class="highlight-yellow">🛡️ Bienes Esenciales (Art. 5)</h3>
            <p>Bienes indispensables para la existencia, estabilidad, conservación y seguridad del edificio, así como los imprescindibles para el uso y disfrute.</p>
            <p><b>Se reputan como esenciales:</b> El terreno, cimientos, estructura, instalaciones generales de servicios, fachadas y los techos o losas de cubierta.</p>
        </div>
        """, unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1503387762-592deb58ef4e?auto=format&fit=crop&w=600&q=80", use_column_width=True)

# ==========================================
# SECCIÓN 3: CRONOLOGÍA (SELECTOR FUTURISTA)
# ==========================================
elif menu == "🚀 Cronología Judicial":
    st.markdown("<h2 class='title-glow' style='text-align: center; margin-bottom: 30px;'>Trazabilidad Legal vs. Taller 7</h2>", unsafe_allow_html=True)
    
    año = st.radio("Seleccione la fase del proceso:", ["2023", "2024", "2025", "2026"], horizontal=True, label_visibility="collapsed")
    st.markdown("<br>", unsafe_allow_html=True)

    if año == "2023":
        st.markdown("""
        <div class="legal-card">
            <h3 class="highlight-yellow">HITOS DEL AÑO 2023</h3>
            <ul>
                <li><b>Marzo 31:</b> En Asamblea General Ordinaria, la constructora Taller Siete entregó a los copropietarios los bienes comunes esenciales y documentación asociada con planos, reglamentos, garantías de equipos, licencias de construcción, manuales de manejo, permisos, entre otros.</li>
                <li><b>Marzo/Abril:</b> En Asambleas Extraordinarias se toma la decisión de contratar a <b>Terrakota Construcciones</b>, con el fin de realizar la consultoría para recibir zonas comunes del Edificio.</li>
                <li><b>Diciembre:</b> En Asamblea Extraordinaria se exige a la administración destinar los recursos recaudos por cuota extraordinaria a la suscripción del contrato con Terrakota, dado que fueron utilizados sin la autorización de la Asamblea.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    elif año == "2024":
        st.markdown("""
        <div class="legal-card">
            <h3 class="highlight-yellow">HITOS DEL AÑO 2024</h3>
            <ul>
                <li><b>Marzo:</b> Entrega informe de interventoría a la copropiedad y a la firma constructora.</li>
                <li><b>Mayo 18:</b> En Asamblea Extraordinaria se socializa Informe de interventoría y se solicita a la administración realizar las gestiones para que se inicien las obras de reparación.</li>
                <li><b>Mayo 31:</b> Mesa de trabajo con delegados de Taller Siete, Terrakota, y el Edificio. <b>Compromiso:</b> la constructora entregaría respuesta al informe de interventoría el 7 de junio.</li>
                <li><b>Julio 3:</b> Derecho de petición solicitando respuesta al Informe, de acuerdo con los compromisos pactados.</li>
                <li><b>Julio 30:</b> Se radica otro derecho de petición reiterando a Taller Siete la solicitud de respuesta requerida en el derecho de petición del 3 de julio.</li>
                <li><b>Agosto 14:</b> Se radica queja ante la Secretaría Distrital del Hábitat (SDHT) por la no entrega de zonas comunes que presentan deficiencias en su funcionalidad con afectaciones a propietarios y residentes.</li>
                <li><b>Octubre 3:</b> Visita de inspección a las zonas comunes por parte de la SDHT.</li>
                <li><b>Octubre 10:</b> Se radica tutela contra Taller 7 por no respuesta a las solicitudes de julio 3 y 30.</li>
                <li><b>Octubre 15:</b> Taller 7 da respuesta al Juzgado 100 de tutela indicando que inician obras en febrero de 2025.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    elif año == "2025":
        st.markdown("""
        <div class="legal-card">
            <h3 class="highlight-yellow">HITOS DEL AÑO 2025</h3>
            <ul>
                <li><b>Marzo 17:</b> Mediante comunicación se solicita a Taller 7 el compromiso de iniciar obras en febrero.</li>
                <li><b>Abril 14:</b> El director del proyecto de Taller 7 presenta propuesta para cubrir el parqueadero piso 1, indicando que la copropiedad debe asumir el 40% de los costos ($26.331.668 x 40% = $10.532.668). La administración y el Consejo convocan a mesas de trabajo.</li>
                <li><b>Junio:</b> Se radica nueva tutela ante el Juzgado 99 penal municipal, ante la no respuesta a las solicitudes de asistir a las mesas de trabajo.</li>
                <li><b>Junio 18:</b> Taller Siete da respuesta a la tutela con copia al Juzgado 99, informando que el Arq. Juan Carlos Vélez es el delegado para participar en las mesas de trabajo.</li>
                <li><b>Junio 26:</b> Mesa de trabajo con Ing. Vélez, el administrador y dos integrantes del Consejo (Francina Ruiz y Nubia Pulido) en la cual sólo se analizó la propuesta de cubrir el piso 1.</li>
                <li><b>Julio 3:</b> Administración y Consejo comunican a Taller 7 la decisión de <b>no aceptar la propuesta de cubrir el parqueadero piso 1</b> por afectaciones técnicas, de diseño y permisos ante curaduría.</li>
                <li><b>Julio 25:</b> Se recibe del Ing. Jaime Cortés López Informe de Hallazgos, patología y recomendaciones para abatir problemas de infiltración.</li>
                <li><b>Agosto 27:</b> Se recibe notificación del Auto 1486 (SDHT) que ordena <b>apertura de la investigación administrativa</b> contra TALLER SIETE por deficiencias constructivas calificadas como <b>AFECTACIÓN GRAVE y GRAVÍSIMA</b>.</li>
                <li><b>Agosto 27:</b> Derecho de petición a Taller 7 solicitando: (i) Garantía Legal o póliza de estabilidad, (ii) Acta de entrega zonas comunes, (iii) Manuales, y (iv) Reparación de daños en elementos esenciales.</li>
                <li><b>Septiembre 27:</b> Al no obtener respuesta, se radica tutela en el Juzgado 67.</li>
                <li><b>Septiembre 29:</b> Taller 7 da respuesta remitiendo 2 pólizas "Todo Riesgo Contratista" <b>VENCIDAS</b> de Aseguradora Solidaria.</li>
                <li><b>Octubre 8:</b> Se envía memorial al Juzgado 67 indicando que la respuesta no fue resuelta de fondo. Nota: El juez desestima la impugnación y cierra la tutela.</li>
                <li><b>Octubre 20:</b> Respuesta de la SDHT informando que la solicitud se incluye en el expediente que cursa en la entidad.</li>
                <li><b>Octubre 22:</b> Se radica solicitud de conciliación civil y comercial en la Procuraduría por incumplimiento en responsabilidad postventa.</li>
                <li><b>Noviembre 19:</b> Derecho de petición a Taller 7 solicitando nuevamente Póliza de Estabilidad de Obra o Garantía Legal.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    elif año == "2026":
        st.markdown("""
        <div class="legal-card">
            <h3 class="highlight-yellow">HITOS DEL AÑO 2026</h3>
            <ul>
                <li><b>Enero 13:</b> Juzgado 13 admite acción de tutela en curso.</li>
                <li><b>Enero 26:</b> Juez Constitucional ordena a Taller 7 emitir respuesta de fondo y congruente.</li>
                <li><b>Enero 28 (Defensa Taller 7):</b> Argumentan que la Garantía Legal (Ley 1480) <i>"no constituye un documento tangible"</i> y niegan obligación de garantía real.</li>
                <li><b>Febrero 10:</b> Administración estructura recurso de <b>impugnación</b> estratégico para desvirtuar la respuesta de la constructora.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# SECCIÓN 4: CONCLUSIONES Y RECOMENDACIONES
# ==========================================
elif menu == "💡 Conclusiones y Recomendaciones":
    st.markdown("<h2 class='title-glow'>Plan de Acción y Resoluciones Estratégicas</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="legal-card">
        <h3 class="highlight-yellow">1. Estado Patrimonial de la Constructora</h3>
        <p>🔎 Una vez se realizan consultas en Catastro Distrital, Instituto Geográfico Agustín Codazzi (IGAC) y Secretaría Distrital de Movilidad, se concluye que <b>Taller 7 no tiene bienes a cargo</b>, por lo que resulta difícil que se pueda proponer interponer una demanda civil.</p>
        <p>Adicionalmente:</p>
        <ul>
            <li>El representante legal Señor Jairo Andrés Jaramillo sólo tiene una casa lote en el municipio de La Mesa (Cundinamarca).</li>
            <li>La segunda representante legal sólo tiene un apartamento en Bogotá.</li>
        </ul>
    </div>
    
    <div class="legal-card">
        <h3 class="highlight-yellow">2. Propuesta de Reparación Interna</h3>
        <p>🏗️ Se propone a los copropietarios la decisión de reparar las zonas comunes. Para esto es necesario:</p>
        <ul>
            <li>Diseñar términos de referencia que permitan que los diferentes ingenieros y arquitectos que la administración ha contactado participen y presenten sus propuestas.</li>
            <li>Dichas propuestas deberán ser evaluadas por el Consejo de Administración y la Administración.</li>
            <li>Presentar los resultados en una Asamblea Extraordinaria para decidir qué proponente contratar.</li>
        </ul>
    </div>
    
    <div class="legal-card">
        <h3 class="highlight-yellow">3. Financiación (Crédito Institucional)</h3>
        <p>🏦 Evaluar la opción de solicitar un crédito a favor del Edificio con el <b>Banco Agrario</b>, una vez se cumplan los siguientes requisitos de la entidad financiera:</p>
        <ul style="column-count: 2; column-gap: 20px;">
            <li>Representación Legal y RUT completo.</li>
            <li>Estados financieros (2022, 2023, 2024 y 2025) con notas y copia de la tarjeta del contador.</li>
            <li>Declaración de renta (2 últimos años).</li>
            <li>Cédula del Representante Legal y su respectiva Declaración de Renta.</li>
            <li>Relación de contratos, clientes y proveedores.</li>
            <li>Copia del acta de la <b>Asamblea General de Copropietarios</b> donde quede expresamente que se autoriza al Consejo y a la Administración solicitar el crédito a favor del Edificio Vivo.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)