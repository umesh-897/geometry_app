import streamlit as st
import time

def triangle_perimiter(a,b,c):
    return a+b+c
def triangle_area(a,b,c):
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c))**(1/2)
    return area

def square_perimeter(side):
    return 4*side

def square_area(side):
    return side**2

def rectangle_perimeter(l,b):
    return 2*(l+b)

def rectangle_area(l,b):
    return l*b

def circle_perimeter(r):
    return 2*(22/7)*r

def circle_area(r):
    return (22/7)*(r**2)

#3d objects

def cone_tsa(r,l):
    return ((22/7)*r*(r+l))

def cone_vol(r,l):
    return (1/3)*(22/7)*(r**2)*((l**2)-(r**2))**(1/2)

def cube_tsa(s):
    return 6*(s**2)

def cube_vol(s):
    return s**3

def cuboid_tsa(l,b,h):
    return 2*(l*b+b*h+h*l)

def cuboid_vol(l,b,h):
    return l*b*h

def sphere_tsa(r):
    return 4*(22/7)*(r**2)

def sphere_volume(r):
    return (4/3)*(22/7)*(r**3)

def cylinder_tsa(r,h):
    return 2*(22/7)*r*(h+r)

def cylinder_vol(r,h):
    return (22/7)*(r**2)*h


st.title('Geometry Calculator')

st.header('2D shapes')

st.subheader('Triangle')

col1,col2=st.columns([1,3])


with col1:
    a=st.number_input('side1: ')
    b=st.number_input('side2:')
    c=st.number_input('side3: ')
    

col_a,col_b=st.columns(2)

with col_a:
    st.metric('Perimeter',triangle_perimiter(a,b,c))
    
with col_b:
    st.metric('Area',triangle_area(a,b,c))
    
##################sqaure

st.divider()

st.subheader('Square')

col1s,col2s=st.columns([1,3])

with col1s:
    s=st.number_input('side: ')


colas,colbs=st.columns(2)

with colas:
    st.metric('Perimeter',square_perimeter(s))

with colbs:
    st.metric('Area',square_area(s))
    
    
###############rectangle

st.divider()

st.subheader('Rectangle')

col1r,col2r=st.columns([1,3])

with col1r:
    l=st.number_input('length: ')
    b=st.number_input('breadth: ')

colar,colbr=st.columns(2)

with colar:
    st.metric('Perimeter',rectangle_perimeter(l,b))

with colbr:
    st.metric('Area',rectangle_area(l,b))




###############circle

st.divider()

st.subheader('circle')

col1c,col2c=st.columns([1,3])

with col1c:
    r=st.number_input('Radius: ',key='col_c')
    

colac,colbc=st.columns(2)

with colac:
    st.metric('Perimeter',round(circle_perimeter(r),2))

with colbc:
    st.metric('Area',round(circle_area(r),2))