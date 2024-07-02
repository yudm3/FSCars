import streamlit as st
import pandas as pd
import numpy as np
from scrape_rates import GetGoogleRates
from datetime import datetime


countries = ["Россия", "Узбекистан", "Кыргызстан", "Казахстан"]
delivery_in_kg = {"types" : ["Обычная", "Экспресс"],
                  "prices" : [2400, 2700],
                  "days" : ["20-22", "24-27"]}
delivery_col_names = ["Сервис", "Цена ($)", "Транзитное время (дни)"]
manufacture_years = ["2024-2022", "2021-2020", "2019 и менее"]
engine_types = ["Двигатель внутреннего сгорания", "Электрический двигатель"]
sum_col_names = ["Цена", "Доставка", "Растаможка", "Услуги"]

rates = {}
if not rates:
    sr = GetGoogleRates()
    sr.fetch_rates()
    rates = sr.get_rates()
    rate_time = datetime.now().strftime("%d/%m/%Y %H:%M")


st.title('FS CAR EXPORT')
st.subheader('_Твой экспортный калькулятор_')
st.write('-----')


price = st.number_input("Цена авто в корейских вонах (KRW)", min_value=0, value=0, key=int,
                        placeholder="Введите цену авто")

country = st.selectbox(
        "Выберите страну для экспорта:flag-ru::flag-uz::flag-kg::flag-kz:",
        (countries),
    )





if country == countries[0]:
    print()

elif country == countries[1]:
    print()

elif country == countries[2]:

    delivery = st.selectbox(
        "Выберите способ доставки",
        (delivery_in_kg["types"]),
    )

    delivery_df = pd.DataFrame(data=delivery_in_kg)
    delivery_df.rename(columns=dict(zip(delivery_in_kg.keys(), delivery_col_names)),
                       inplace=True)
    delivery_df.index += 1 
    st.table(delivery_df)

    engine_type = st.selectbox(
        "Выберите тип двигателя",
        (engine_types),
    )

    manufacture_year = ""
    if engine_type == engine_types[0]:
        manufacture_year = st.selectbox(
            "Выберите год выпуска автомобиля",
            (manufacture_years),
        )

    # Regular + 22+
    if engine_type == engine_types[0] and manufacture_year == manufacture_years[0]:
        pass
    # Regular + 20-21
    elif engine_type == engine_types[0] and manufacture_year == manufacture_years[1]:
        pass
    # Regular + 19-
    elif engine_type == engine_types[0] and manufacture_year == manufacture_years[2]:
        pass
    # Electro
    elif engine_type == engine_types[1]:
        pass
    else:
        st.write("Invalid Engine Choice!")

    calc_button = st.button("Рассчитать сумму", type="primary")

    if calc_button:
        st.write("-----")
        st.dataframe(pd.DataFrame(data=rates), hide_index=True)
        st.markdown(f"Курсы валют получены с сайта _www.google.com/finance/quote/KRW-USD_ в {rate_time}")

        # sum_df = pd.DataFrame(data=delivery_in_kg)
        # sum_df.rename(columns=dict(zip(delivery_in_kg.keys(), delivery_col_names)),
        #                 inplace=True)
        # sum_df.index += 1
        # st.table(sum_df)

    

elif country == countries[3]:
    print()

else:
    st.write("Invalid Country Choice!")