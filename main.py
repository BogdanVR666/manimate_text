import streamlit as st

python_code = r'''
def hello():
    print("Hello, World!")

if __name__ == "__main__":
    hello()
'''

latex_code = r"""
\begin{pmatrix}
1 & 2 \\
3 & 4 \\
\end{pmatrix}
"""

st.title("My First test app")

manim_tab, LaTeX_tab = st.tabs(["manim", "LaTeX"])

with manim_tab:
    st.write("От так можна анімувати код")
    st.write("Сам код:")
    st.code(python_code, language="python")
    st.write("Його анімація:")
    st.video("static/videos/code_animation.mp4")

with LaTeX_tab:
    st.write("Якщо в LaTeX написати приблизно наступний код:")
    st.code(latex_code, language="latex")
    st.write("то буде наступний вивід:")
    st.latex(latex_code)
    st.write("Слід зауважити, що від першої літери назви матриці залежить форма її дужок")
    st.write("Ось наприклад що буде якщо замінити **p** на **b**, або на **v**")

    left_column, right_column = st.columns(2)
    with left_column:
                st.latex(latex_code.replace("p", "b"))

    with right_column:
        st.latex(latex_code.replace("p", "v"))