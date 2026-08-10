import streamlit as st

# ==========================================
# CONFIGURACIÓN DE LA PÁGINA
# ==========================================
st.set_page_config(page_title="Operaciones Unitarias", page_icon="🏭", layout="wide")

# ==========================================
# TEXTO DEL REPORTE PARA DESCARGAR
# ==========================================
REPORTE_TEXTO = """RESUMEN DE OPERACIONES UNITARIAS Y EQUIPOS

1. TRANSPORTE DE FLUIDOS
- Bombas: Balance de Energía Mecánica (Bernoulli). Diseño: Potencia = Q * dP / Eficiencia.
- Compresores: Trabajo de compresión adiabática. Variables clave: Relación de compresión, caudal.

2. TRANSFERENCIA DE CALOR
- Intercambiadores: Balance Q = m * Cp * dT. Diseño: Q = U * A * F * DTml.
- Variables: U, Área, Temperaturas. T y P afectan el estado termodinámico y estrés de materiales.

3. TRANSFERENCIA DE MASA Y SEPARACIÓN
- Tanque Flash: Balances globales y Ecuación de Rachford-Rice.
- Destilación: Ecuaciones de McCabe-Thiele. Variables: Reflujo, Etapas, Volatilidad.
- Evaporadores: Balance térmico mv * lambda = U * A * dT. Variables: Economía, Área.
- Cristalizadores: Curvas de solubilidad y grado de sobresaturación.
- Secadores: Velocidad de secado y psicrometría.

4. REACTORES QUÍMICOS
- Ecuación cinética: -rA = k(T) * C^n (Arrhenius dicta el efecto de T).
- Batch: t = N_A0 * integral(dX_A / -r_A * V)
- CSTR (Mezcla Completa): V = (F_A0 * X_A) / -r_A
- PFR (Flujo Pistón): V = F_A0 * integral(dX_A / -r_A)
"""

# ==========================================
# BARRA LATERAL (SIDEBAR)
# ==========================================
with st.sidebar:
    st.header("⚙️ Operaciones Unitarias")
    seccion = st.radio(
        "Selecciona una categoría:",
        ["Transporte de Fluidos", 
         "Transferencia de Calor", 
         "Transferencia de Masa", 
         "Reactores Químicos"]
    )
    
    st.divider()
    st.markdown("📥 **Descargar Apuntes**")
    st.download_button(
        label="Descargar Resumen (.txt)",
        data=REPORTE_TEXTO,
        file_name="resumen_operaciones_unitarias.txt",
        mime="text/plain",
        type="primary"
    )

# ==========================================
# CONTENIDO PRINCIPAL
# ==========================================
st.title("🏭 Manual de Equipos de Proceso")
st.markdown("Ecuaciones de diseño, balances y parámetros operativos clave.")
st.divider()

if seccion == "Transporte de Fluidos":
    st.header("💧 Transporte de Fluidos")
    st.markdown("*El enfoque principal recae en el balance de energía mecánica.*")
    
    st.subheader("Bombas (Centrífugas y Desplazamiento Positivo)")
    st.markdown("**Ecuación Fundamental (Bernoulli):**")
    st.latex(r"\frac{\Delta P}{\rho} + \frac{\Delta v^2}{2} + g\Delta z + h_f = \frac{\dot{W}_{bomba}}{\dot{m}}")
    st.markdown("**Ecuación de Diseño (Potencia):**")
    st.latex(r"Potencia = \frac{Q \cdot \Delta P}{\eta}")
    st.info("**Variables a definir:** Caudal volumétrico ($Q$), eficiencia ($\eta$), diferencia de presión ($\Delta P$).")
    st.warning("**Efecto P y T:** Mayor $T$ baja la densidad y sube la presión de vapor, reduciendo el NPSH disponible (riesgo de cavitación).")

    st.divider()
    st.subheader("Compresores y Sopladores")
    st.markdown("**Ecuación Fundamental (Trabajo Adiabático Ideal):**")
    st.latex(r"W = \frac{k}{k-1} P_1 V_1 \left[ \left(\frac{P_2}{P_1}\right)^{\frac{k-1}{k}} - 1 \right]")
    st.info("**Variables a definir:** Relación de compresión ($P_2/P_1$), coeficiente adiabático ($k$), caudal, eficiencia isoentrópica.")

elif seccion == "Transferencia de Calor":
    st.header("🔥 Transferencia de Calor")
    
    st.subheader("Intercambiadores de Calor")
    st.markdown("**Balance de Energía Térmica:**")
    st.latex(r"Q = \dot{m}_{c}C_{p,c}(T_{c,out} - T_{c,in}) = \dot{m}_{h}C_{p,h}(T_{h,in} - T_{h,out})")
    st.markdown("**Ecuación de Diseño:**")
    st.latex(r"Q = U \cdot A \cdot F \cdot \Delta T_{ML}")
    st.info("**Variables a definir:** Coeficiente global ($U$), área ($A$), factor de corrección ($F$), Temperaturas.")
    st.warning("**Efecto P y T:** La $\Delta T$ es la fuerza impulsora. Altas presiones obligan a usar paredes de tubos más gruesas, aumentando la resistencia térmica y reduciendo el $U$.")

elif seccion == "Transferencia de Masa":
    st.header("⚗️ Transferencia de Masa y Separación")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Tanque Flash")
        st.markdown("**Balance y Rachford-Rice:**")
        st.latex(r"F = V + L")
        st.latex(r"\sum_{i=1}^{c} \frac{z_i(K_i - 1)}{1 + \Psi(K_i - 1)} = 0")
        st.info("**Variables:** Fracción vaporizada ($\Psi=V/F$), Constantes de equilibrio ($K_i$). $P$ y $T$ son las variables absolutas de control.")
        
        st.subheader("Cristalizadores")
        st.markdown("**Rendimiento ($Y$):**")
        st.latex(r"Y = W \cdot \left[ \frac{C_1 - C_2}{100 - C_2} \right]")
        st.info("**Variables:** Temperatura de enfriamiento, sobresaturación.")

    with col2:
        st.subheader("Columna de Destilación")
        st.markdown("**Línea de Operación (McCabe-Thiele):**")
        st.latex(r"y_{n+1} = \frac{R}{R+1}x_n + \frac{x_D}{R+1}")
        st.info("**Variables:** Reflujo ($R$), N° de etapas, plato de alimentación, volatilidad relativa ($\alpha$).")
        
        st.subheader("Evaporadores")
        st.markdown("**Transferencia Térmica:**")
        st.latex(r"\dot{m}_v \cdot \lambda_v = U \cdot A \cdot (T_{vap} - T_{ebull})")
        st.info("**Variables:** Economía, Área, Elevación del Punto de Ebullición (EPE).")

elif seccion == "Reactores Químicos":
    st.header("🧪 Reactores Químicos")
    st.markdown("La cinética general es $-r_A = k(T) \cdot C_A^n$. El efecto de $T$ se rige por **Arrhenius** ($k = A \cdot e^{-E_a/RT}$).")
    
    st.subheader("Reactor Batch (Discontinuo)")
    st.latex(r"t = N_{A0} \int_{0}^{X_A} \frac{dX_A}{(-r_A)V}")
    
    st.subheader("CSTR (Mezcla Completa Continua)")
    st.latex(r"V = \frac{F_{A0} \cdot X_A}{-r_A}")
    
    st.subheader("PFR (Flujo Pistón)")
    st.latex(r"V = F_{A0} \int_{0}^{X_A} \frac{dX_A}{-r_A}")
