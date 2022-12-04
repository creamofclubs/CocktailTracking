import tools as t
import streamlit as st

st.sidebar.title('Options')

#print(tools.alcohol_by_volume(105,37,15,2))

option = st.sidebar.selectbox('Select your options',('Tools', 'Bargin Grab'))
placeholder = 0

if option == 'Tools':
    tools = st.sidebar.selectbox('Select your tool',('Alcohol Dilution', 'Spirit ABV'))
    if tools == 'Alcohol Dilution':
        st.header('Cocktail Tools')
        st.subheader('Alcohol Dilution test')
        st.write('If you dont know the total alcohol ABV, please use the Spirit ABV tool. ')
        alc_volume = st.number_input('Enter volume of Alcohol in ml, ie: Spirits and Liqueurs',0)
        abv = st.number_input('Enter ABV. ie 35 will equal 35%',0.0)
        nonalc_volume = st.number_input('Enter volume of non alcohol items, ie: Juices and syrups',0)
        iceselect = st.selectbox('Select your ice option.',('No Ice', 'Shaken','Stired','Whip Shaken','Lightly Shaken'),index=1)
        if iceselect == 'No Ice':
            ice = 0
        elif iceselect == 'Shaken':
            ice = 1
        elif iceselect == 'Stired':
            ice = 2
        elif iceselect == 'Whip Shaken':
            ice = 3
        elif iceselect == 'Lightly Shaken':
            ice = 4
        else:
            ice = -1

        try:
            result = t.alcohol_by_volume(alc_volume,abv,nonalc_volume,ice)
            res = round((result[0] * 100),3)
            total_volume = round((result[4]))
            st.write(f'Your cocktail volume will be {total_volume}ml.')
            st.write(f'Total ABV % of your cocktail will be {res}% approximately.')
            st.write(f'Alcohol units of your cocktail will be {result[1]} approximately.')
            st.write(f'Proof UK will be {result[2]} approximately.')
            st.write(f'Proof US will be {result[3]} approximately.')
        except ZeroDivisionError:
            pass
    
    if tools == 'Spirit ABV':
        st.header('Cocktail Tools')
        st.subheader('Spirit ABV')
        st.write("This will calculate the ABV, of all alcoholic content. For example 35ml of vodka @ 37% and 30ml and  kahlua @ 20%")
        col1, col2 ,col3= st.columns(3)
        c1vol = col1.number_input('R1 volume ml',0)
        c1abv = col2.number_input('R1 ABV')
        c2vol = col1.number_input('R2 volume ml',0)
        c2abv = col2.number_input('R2 ABV')
        c3vol = col1.number_input('R3 volume ml',0)
        c3abv = col2.number_input('R3 ABV')
        c4vol = col1.number_input('R4 volume ml',0)
        c4abv = col2.number_input('R4 ABV')
        c5vol = col1.number_input('R5 volume ml',0)
        c5abv = col2.number_input('R5 ABV')

        v1 = t.aclcohol_pct(c1vol,c1abv)
        v2 = t.aclcohol_pct(c2vol,c2abv)
        v3 = t.aclcohol_pct(c3vol,c3abv)
        v4 = t.aclcohol_pct(c4vol,c4abv)
        v5 = t.aclcohol_pct(c5vol,c5abv)
        total_alc = v1+v2+v3+v4+v5
        
        total_vol = c1vol + c2vol + c3vol + c4vol + c5vol
        try:
            results = round(total_alc,2) /total_vol
            r = round((results * 100),2)
            st.write(f'Total Volume {total_vol}ml and total alcohol {total_alc}ml')
            st.write(f'ABV of all Alcohol Content is {r}%')
        except ZeroDivisionError:
            pass
        

   



if option == 'Bargin Grab':
    st.header('Bargin Grab')
    st.subheader('Coming soon')
    stores = st.sidebar.selectbox('Select your store',('Drink Stuff', 'Tesco'))
