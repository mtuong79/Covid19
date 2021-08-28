import streamlit as st

st.header("COVID19 BOOK")
st.image("img/1022.png")

st.subheader("[ĐƯỜNG DÂY NÓNG](https://covid19.hochiminhcity.gov.vn/duong-day-nong-thanh-pho)")
xem_yte = st.radio("",
                   ('Q10-YTe Luu Dong','Q10-SOS','Q10-Yte','Q3-Yte','Q3-SOS'))
if xem_yte == 'Q10-YTe Luu Dong':
    st.image("img/q10-YTeDong.png")
elif xem_yte == 'Q10-SOS':
    st.image("img/q10-p2-SOS.png")
elif xem_yte == 'Q10-Yte':
    st.image("img/q10-YTe.jpg")
elif xem_yte == 'Q3-Yte':
    st.image("img/q3-YTe.jpg")
else:
    st.image("img/q3-p3-SOS.png")

st.subheader("DINH DUONG LA VANG")
xem_dd = st.radio("",('Dinh Duong','Thuc Pham'))
if xem_dd == 'Dinh Duong':
    st.image("img/STSK-DinhDuong.png")
elif xem_dd == 'Thuc Pham':
    st.image("img/STSK-ThucPham.png")

st.subheader("Trieu Chung va Dieu Tri Covid")
xem_covid = st.radio("", ('Trieu Chung','Dieu Tri F0','Cap Cuu'))
if xem_covid == 'Trieu Chung':
    st.image("img/STSK-TrieuChung.png")
elif xem_covid == 'Dieu Tri F0':
    st.image("img/STSK-F0.png")
else:
    st.image("img/STSK-CapCuu.png")

st.subheader("TIM HIEU THEM")
st.write("Cong thong tin Covid19 [HCM](https://covid19.hochiminhcity.gov.vn/home)")
st.write("[Sổ tay](https://covid19.hochiminhcity.gov.vn/cham-soc-suc-khoe/-/asset_publisher/ZSHLi888uq2s/content/so-tay-suc-khoe-covid--1?inheritRedirect=false&redirect=https%3A%2F%2Fcovid19.hochiminhcity.gov.vn%2Fcham-soc-suc-khoe%3Fp_p_id%3D101_INSTANCE_ZSHLi888uq2s%26p_p_lifecycle%3D0%26p_p_state%3Dnormal%26p_p_mode%3Dview%26p_p_col_id%3Dcolumn-10%26p_p_col_count%3D1) sức khỏe Covid 19")