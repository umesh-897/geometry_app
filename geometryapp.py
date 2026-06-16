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
    
#######################cone
st.divider()
st.divider()

st.header('3D Objects')
st.subheader('Cone')

col1co,col2co=st.columns([1,3])

with col1co:
    r_cone=st.number_input('Radius: ',key='cone_r')
    l_cone=st.number_input('Lateral side Length: ',key='cone_l')

colaco,colbco=st.columns(2)

with colaco:
    st.metric('Total Surface Area',cone_tsa(r_cone,l_cone))

with colbco:
    st.metric('Volume',cone_vol(r_cone,l_cone))
    
    
#######################cube
st.divider()
st.divider()


st.subheader('Cube')

col1cu,col2cu=st.columns([1,3])

with col1cu:
    s_cube=st.number_input('Radius: ',key='col_cu')
    

cubeacu,cubebcu=st.columns(2)

with cubeacu:
    st.metric('Total Surface Area',cube_tsa(s_cube))

with cubebcu:
    st.metric('Volume',cube_vol(s_cube))
    
    


#######################cuboid
st.divider()
st.divider()


st.subheader('Cuboid')

col1boid,col2boid=st.columns([1,3])

with col1boid:
    l=st.number_input('Length: ',key='cuboid_l')
    b=st.number_input('Breadth: ',key='cuboid_b')
    h=st.number_input('Height : ',key='cuboid_c')

cola_boid,colb_boid=st.columns(2)

with cola_boid:
    st.metric('Total_suraface_Area',cuboid_tsa(l,b,h))

with colb_boid:
    st.metric('Volume',cuboid_vol(l,b,h))
    
    

###############Sphere
st.divider()
st.divider()


st.subheader('Sphere')

col1_sp,col2_sp=st.columns([1,3])

with col1_sp:
    r_sphere=st.number_input('Radius: ',key='sphere')
   

cola_sp,colb_sp=st.columns(2)

with cola_sp:
    st.metric('Total Surface Area',round(sphere_tsa(r_sphere)),2)

with colb_sp:
    st.metric('Volume',round(sphere_volume(r_sphere)),2)
    
    
    
##################Cylinder    

st.divider()
st.divider()


st.subheader('Cylinder')

col1co,col2co=st.columns([1,3])

with col1co:
    r_cyl=st.number_input('Radius: ',key='r_cyl')
    h_cyl=st.number_input('Height: ',key='h_cyl')

cola_cyl,colb_cyl=st.columns(2)

with cola_cyl:
    st.metric('Total Surface Area',cylinder_tsa(r_cyl,h_cyl))

with colb_cyl:
    st.metric('Volume',cylinder_vol(r_cyl,h_cyl))
    
    
