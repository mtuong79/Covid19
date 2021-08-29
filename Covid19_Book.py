import streamlit as st

st.header("COVID19 BOOK")
st.image("img/1022.png")

st.subheader("[ĐƯỜNG DÂY NÓNG](https://covid19.hochiminhcity.gov.vn/duong-day-nong-thanh-pho)")
xem_yte = st.radio("",
                   ('Q10-Y Tế Lưu Động','Q10-Tổ phản ứng nhanh F0','Q10-Y Tế','Q3-Y Tế','Q3-Tổ phản ứng nhanh F0','Hỗ trợ nhu yếu phẩm'))
if xem_yte == 'Q10-Y Tế Lưu Động':
    st.image("img/q10-YTeDong.png")
elif xem_yte == 'Q10-Tổ phản ứng nhanh F0':
    st.image("img/q10-p2-SOS.png")
elif xem_yte == 'Q10-Y Tế':
    st.image("img/q10-YTe.jpg")
elif xem_yte == 'Q3-Tổ phản ứng nhanh F0':
    st.image("img/q3-YTe.jpg")
elif:
    st.image("img/q3-p3-SOS.png")
else:
    st.image("img/SOS-ThucPham.png")

st.subheader("DINH DƯỠNG LÀ VÀNG")
xem_dd = st.radio("",('Dinh Dưỡng','Thực Phẩm'))
if xem_dd == 'Dinh Dưỡng':
    st.image("img/STSK-DinhDuong.png")
elif xem_dd == 'Thực Phẩm':
    st.image("img/STSK-ThucPham.png")

st.subheader("Triệu Chứng và Điều Trị")
xem_covid = st.radio("", ('Triệu Chứng','Điều Trị F0','Cấp Cứu'))
if xem_covid == 'Triệu Chứng':
    st.image("img/STSK-TrieuChung.png")
elif xem_covid == 'Điều Trị F0':
    st.image("img/STSK-F0.png")
else:
    st.image("img/STSK-CapCuu.png")

st.subheader("TÌM HIỂU THÊM")
st.write("Cổng thông tin Covid19 [HCM](https://covid19.hochiminhcity.gov.vn/home)")
st.write("[Sổ tay](https://covid19.hochiminhcity.gov.vn/cham-soc-suc-khoe/-/asset_publisher/ZSHLi888uq2s/content/so-tay-suc-khoe-covid--1?inheritRedirect=false&redirect=https%3A%2F%2Fcovid19.hochiminhcity.gov.vn%2Fcham-soc-suc-khoe%3Fp_p_id%3D101_INSTANCE_ZSHLi888uq2s%26p_p_lifecycle%3D0%26p_p_state%3Dnormal%26p_p_mode%3Dview%26p_p_col_id%3Dcolumn-10%26p_p_col_count%3D1) sức khỏe Covid 19")
st.write("[Giúp Tôi](https://www.giuptoi.vn/) - Kết Nối và Trợ Giúp")
st.write("Bệnh viện Chợ Rẫy khám bệnh [online](https://thanhnien.vn/thoi-su/benh-vien-cho-ray-kham-benh-online-tu-9-gio-hom-nay-128-cho-cac-bn-khong-phai-benh-covid-19-1429436.html)")
