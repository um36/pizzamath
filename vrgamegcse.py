# Updated data for topic links, difficult topics, and VR benefits
##########################

# Data structure for content weightings (based on provided midpoints)
data = {
    "Foundation": {
        "AQA": [25, 20, 25, 15, 15],  # AQA percentages for Foundation
        "OCR": [25, 20, 25, 15, 15],  # OCR percentages for Foundation
        "Edexcel": [25, 20, 25, 15, 15]  # Edexcel percentages for Foundation (midpoints)
    },
    "Higher": {
        "AQA": [15, 30, 20, 20, 15],  # AQA percentages for Higher
        "OCR": [15, 30, 20, 20, 15],  # OCR percentages for Higher
        "Edexcel": [15, 30, 20, 20, 15]  # Edexcel percentages for Higher (midpoints)
    }
}

# Custom CSS for Pizza Theme
st.markdown(
    """
    <style>
    /* Set the entire app's background color */
    .stApp {
        background-color: #fbe8d3; /* Light beige (pizza dough) */
    }

    /* Style the expanders */
    [data-testid="st-expander"] {
        background-color: #ff6347; /* Tomato red */
        border: 2px solid #f4e04d; /* Cheese yellow */
        border-radius: 12px;
        box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.2);
        padding: 10px;
    }

    /* Header inside expanders */
    [data-testid="st-expander"] > div:first-child {
        color: #c0392b; /* Pepperoni red */
        font-size: 1.2em;
        font-weight: bold;
        text-shadow: 1px 1px #f4e04d; /* Cheese shadow */
    }

    /* Text inside expanders */
    [data-testid="st-expander-content"] {
        color: #5a3e2b; /* Crust brown */
        font-size: 1em;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Labels for the 5 topics
topics = ["Number", "Algebra", "Ratio, Proportion and Rates of Change", "Geometry and Measures", "Statistics"]

st.title('🍕 PIZZA MATHS! 🍕')

# Tabs with added gaming emoji
tab1, tab2, tab3 = st.tabs(["📊 General Research", "🔍 Specific Research", "🎮 Choice of Topic"])

with tab1:
    st.title('📊 General Research')
    st.subheader("📈 Content Weightings Visualisation")
    # Colorful selectbox for user interaction
    level = st.selectbox("Select Exam Level", ["Foundation", "Higher"], label_visibility='visible', key='level')

    exam_boards = st.multiselect("Select Exam Boards", ["AQA", "OCR", "Edexcel"], 
                                 default=["AQA", "OCR", "Edexcel"], 
                                 label_visibility='visible', 
                                 key='exam_boards')

    def plot_pie_chart(exam_board, percentages, ax):
        wedges, texts, autotexts = ax.pie(
            percentages,
            autopct='',  # Do not show percentages inside the pie chart
            startangle=90,
            colors=["#FFB347", "#FF6961", "#77DD77", "#CFCFC4", "#AEC6CF"]  # Pizza colors
        )
        ax.set_title(f"{exam_board} - {level} (Total: {sum(percentages)}%)", color="#D2691E")  # Brown text
        for i, wedge in enumerate(wedges):
            angle = (wedge.theta2 + wedge.theta1) / 2.0
            x = wedge.r * 0.5 * np.cos(np.deg2rad(angle))
            y = wedge.r * 0.5 * np.sin(np.deg2rad(angle))
            ax.text(x, y, str(percentages[i]), ha='center', va='center', fontsize=10)

    fig, axes = plt.subplots(1, len(exam_boards), figsize=(5 * len(exam_boards), 5))
    if len(exam_boards) == 1:
        axes = [axes]
    level_data = data[level]
    for i, exam_board in enumerate(exam_boards):
        plot_pie_chart(exam_board, level_data[exam_board], axes[i])

    plt.tight_layout()
    st.pyplot(fig)

    st.write('📚 **Insights:** Exam boards have consistent topic weightings. Higher levels focus more on Algebra and Geometry, while Foundation leans towards Ratio. Differentiating by level will help refine our approach.')

    st.subheader("🧮 GCSE Syllabus Breakdown")
    # Added relevant emoji for expanders
    with st.expander("📐 Algebra"):
        st.write("""
        - **A1:** Simplifying expressions ✏️
        - **A2:** Solving linear equations 🧮
        - **A3:** Using algebraic formulas 📝
        """)

    with st.expander("🔢 Number"):
        st.write("""
        - **N1:** Understanding place value 🧮
        - **N2:** Operations with fractions and decimals 🍕
        - **N3:** Percentages and ratio 📈
        """)

    # Ratio, Proportion and Rates of Change Expander
    with st.expander("📊 Ratio, Proportion and Rates of Change"):
        st.write("""
        - **R1:** Understanding ratios 📐
        - **R2:** Proportions and scaling 📏
        - **R3:** Direct and inverse variation 🔁
        - **R4:** Solving problems involving ratio and proportion ➗
        - **R5:** Using proportions in real-life contexts 🌍
        - **R6:** Comparing quantities using ratios ⚖️
        """)

    # Geometry and Measures Expander
    with st.expander("🔺 Geometry and Measures"):
        st.write("""
        - **G1:** Properties and constructions 🏗️
        - **G2:** Angle properties 🔺
        - **G3:** Congruence and similarity 🔄
        - **G4:** Area and volume calculations 📏📐
        - **G5:** Understanding transformations 🔄
        - **G6:** Working with 2D and 3D shapes 📦
        """)

    # Probability Expander
    with st.expander("🎲 Probability"):
        st.write("""
        - **P1:** Understanding probability concepts 🎯
        - **P2:** Collecting and interpreting data 📊
        - **P3:** Representing data using graphs and charts 📈
        - **P4:** Measures of central tendency (mean, median, mode) 📅
        - **P5:** Understanding distributions 📊
        - **P6:** Using probability in real-life situations 🌍
        """)

    # Edexcel Examiner Report Section
    st.subheader("📚 Edexcel Examiner Report")

    # Edexcel Paper 1 Expander
    with st.expander("📄 Edexcel Paper 1"):
        st.write("""
        - Take care when carrying out arithmetic operations and check their working to avoid careless errors 🧮.
        - Consider whether or not an answer is reasonable and of a sensible size ⚖️.
        - Read each question carefully and ensure that their final answer matches the question asked 📖.
        - Show their methods clearly when using graphs 📊.
        - Ensure that they know the difference between surface area and volume 🧱.
        - Practise working out an estimate for the mean from a grouped frequency table 📅.
        - Practise answering probability questions that require the use of algebra and ratio 🔢.
        """)

    # Edexcel Paper 2 Expander
    with st.expander("📄 Edexcel Paper 2"):
        st.write("""
        - Should improve their use of calculators in general, particularly for complex calculations involving powers or fractions 🔢.
        - Learn correct geometrical terms and use these when giving reasons in geometry questions 🔺.
        - Work on more efficient methods when working with percentages with a calculator, and avoid using ‘non-calculator’ methods 📱.
        - Ensure they do not round prematurely in multistep calculations to avoid answers outside the acceptable accuracy range ⚖️.
        - Check answers make sense in the context of the question ✔️.
        """)

    # Edexcel Paper 3 Expander
    with st.expander("📄 Edexcel Paper 3"):
        st.write("""
        - Carry out a common-sense check on the answers to calculations 🧠.
        - Read questions expecting a written explanation carefully and ensure the answer matches the question 📖.
        - Practise less straightforward problems that combine algebra, geometry, or probability with ratio ➗.
        - Improve skills in dealing with unit conversions 🔄.
        - Ensure understanding of how to write down an error interval when a number is truncated ✂️.
        - Practise writing proofs of congruence in geometry 🔲.
        """)

    # AQA Examiner Report Section
    st.subheader("📚 AQA Examiner Report")

    # AQA Paper 1 Higher Expander
    with st.expander("📄 AQA Paper 1 Higher"):
        st.subheader("🌟 Topics Where Students Excelled")
        st.write("""
        - Solving basic inequalities ➗
        - Setting up and solving an equation ✖️
        - Standard form 🔢
        - Fractions and ratio ⚖️
        """)
        st.subheader("⚠️ Topics Where Students Struggled")
        st.write("""
        - Surface area 🌐
        - Functions 🔢
        - Product rule for counting 🔢
        - Average speed algebraically 🚗
        """)

    # AQA Paper 1 Foundation Expander
    with st.expander("📄 AQA Paper 1 Foundation"):
        st.subheader("🌟 Topics Where Students Excelled")
        st.write("""
        - Multiples 🔢
        - Addition and division ➕➗
        - Multiplication involving negatives ➖
        - Cubing a given number 🔲
        - Money problem given in a context 💰
        - Substitution 🔄
        - Converting using a given conversion factor 🔄
        - Bar chart involving a ratio 📊
        """)
        st.subheader("⚠️ Topics Where Students Struggled")
        st.write("""
        - Sharing a ratio in the context of angles on a straight line ↔️
        - Substitution and rearranging using negative numbers ➖
        - Powers of 2 🔢
        - Criticising the graph of y = 1/x 📉
        - Division of fractions involving a mixed number ➗
        """)

    # AQA Paper 2 Higher Expander
    with st.expander("📄 AQA Paper 2 Higher"):
        st.subheader("🌟 Topics Where Students Excelled")
        st.write("""
        - Simple ratio ➗
        - Triangular numbers 🔺
        - Money and ratio problem 💰
        - Probability spinner problem 🎡
        - Showing that rectangles are similar 🔲
        - Expanding brackets ⬛
        - Calculating an angle at the circumference 🔵
        """)
        st.subheader("⚠️ Topics Where Students Struggled")
        st.write("""
        - Statistical explanations 📊
        - Explanation involving circle theorems 🔵
        - Probability cards problem 🎴
        - Describing a transformation of a graph 📈
        """)

    # AQA Paper 2 Foundation Expander
    with st.expander("📄 AQA Paper 2 Foundation"):
        st.subheader("🌟 Topics Where Students Excelled")
        st.write("""
        - Using a number line ➡️
        - Simplifying expressions ➗
        - Number properties, factors and primes 🔢
        - Money problem 💰
        - Percentage change problem 💵
        - Sample space and probability 🎲
        """)
        st.subheader("⚠️ Topics Where Students Struggled")
        st.write("""
        - Perimeter by counting squares 🔲
        - Probability problem solving 🎲
        - Evaluating a method 🔍
        - Factorising an expression 🔢
        - Change of compound units 🔄
        """)

    # AQA Paper 3 Higher Expander
    with st.expander("📄 AQA Paper 3 Higher"):
        st.subheader("📈 Topics Where Students Excelled")
        st.write("""
        - Converting a decimal to a fraction 🧮
        - Solving a linear equation ➗
        - Sharing money in a ratio 💵
        - Trigonometry 🔺
        - Estimation calculation 📏
        - Using a relative frequency to find a number of outcomes 🎲
        - Pythagoras’ theorem and area of a triangle 🔺
        """)
        st.subheader("📉 Topics Where Students Struggled")
        st.write("""
        - Using a map ratio with conversion of units 🌍➡️📐
        - Drawing a smooth quadratic curve 📉
        - Interpreting results from a biased spinner 🎯
        - Distance-speed-time calculations in a given context 🚗🕒
        - Taxation and National Insurance calculation 💰
        - Solving a composite function equation 🧑‍🏫
        - Algebraic proof 🧑‍🔬
        - Interpreting a 3D shape from front and side elevations 📐
        - Enlargement with a negative fractional scale factor 🔁
        """)

    # AQA Paper 3 Foundation Expander
    with st.expander("📄 AQA Paper 3 Foundation"):
        st.subheader("📈 Topics Where Students Excelled")
        st.write("""
        - Solving simple equations ➗
        - Mode, median and range calculations 📊
        - Term-to-term rules of a sequence 🔢
        - Distance-time graph 🚶‍♂️⏱️
        - Rates of pay problem 💼
        - Simplifying expressions 🧮
        - Inequality problem solving ⚖️
        - Number problem with proportion ➗
        - Ratio problem with money 💰
        """)
        st.subheader("📉 Topics Where Students Struggled")
        st.write("""
        - Ratio of angles around a point problem solving with AO2 ‘show that’ reasoning 🔵
        - Explanation or comparison AO2 questions involving geometrical reasoning 🔺
        - Area problem with comparison of the area of a triangle and a rectangle ➗
        - Compound percentage decrease 💸
        - Quadratic table of values and plotting a quadratic graph 📉
        - Interpreting a pie chart in the context of an AO3 problem solving question 🍰
        - Trigonometry calculation of a missing side 🔺
        - Estimation with rounding to one significant figure 🔢
        - Explanation AO2 question involving estimation 📏
        - Factorising quadratic expression ➗
        - Solving a bracketed quadratic equation 🧑‍🏫
        """)
    st.subheader('📚 Documentation')
    st.write("For information on the web application, visit [Streamlit Docs](https://docs.streamlit.io).")
    st.write("For information on the specifications for each exam board, visit [AQA](https://www.mymathscloud.com/api/download/modules/GCSE-iGCSE-O-Level/Syllabi/AQA/AQA%208300%20Syllabus.pdf?id=21365792), [Edexcel](https://qualifications.pearson.com/content/dam/pdf/GCSE/mathematics/2015/specification-and-sample-assesment/gcse-maths-2015-specification.pdf),[OCR](https://www.ocr.org.uk/Images/168982-specification-gcse-mathematics.pdf).")
    st.write("For information on examiner reports, visit [AQA report](https://www.aqa.org.uk/subjects/mathematics/gcse/mathematics-8300/assessment-resources?secondaryResourceType=Examiner+reports), [Edexcel report](https://qualifications.pearson.com/content/dam/pdf/GCSE/mathematics/2015/exam-materials/GCSE-Maths-Chief-Examiner-Report-June-2019.pdf).")

with tab2:
    st.title('🔬 Specific Research')
    st.subheader("📚 Topics that link to VR")

        # Area/volume
    with st.expander("Area/Volume 📏"):
        st.write("""
        Teaching these topics through VR allows students to fully immerse themselves in the problem and visualize real-world applications. Area is often a challenging topic for teachers to explain, and VR can provide an engaging, hands-on experience for students. 📐
        """)

    # Number Based Problems
    with st.expander("Number Based Problems 🔢"):
        st.write("""
        Although these are taught well traditionally, students who struggle with conventional learning methods may benefit from VR as it makes understanding basic number concepts feel more intuitive and less intimidating. 🔢
        """)

    # Circular-based Problems (e.g., Pizza)
    with st.expander("Circular-Based Problems (e.g., Pizza) 🍕"):
        st.write("""
        Topics involving circles, such as area, circle theorems, and segments, can be challenging for students, especially when algebra is involved. Using VR to represent these problems with relatable items, like pizzas, allows students to engage in a fun environment and better grasp these concepts. 🍕
        """)

    # Graphs and Quadratics
    with st.expander("Graphs and Quadratics 📊"):
        st.write("""
        Students often find it difficult to plot graphs and understand concepts like the y-intercept, axis, and stationary points. In VR, they could experience these concepts in an immersive way, with life-sized graphs that allow them to walk through and explore each key term and its relevance. 📉
        """)

    # Money Based Problems
    with st.expander("Money Based Problems 💰"):
        st.write("""
        Although generally well understood, money-based problems are common in the GCSE specification. VR can bring these problems to life in real-world scenarios, helping students understand the practical applications and purposes behind these mathematical concepts. 💰
        """)
    st.subheader("✨ Expansion of ratio topic from Version 1")

    # Ratios of areas of pizza
    with st.expander("Ratios of Areas of Pizza - Slices and Pricing 🍕➗💵"):
        st.write("""
        Explore ratios through the concept of pizza slices. For example, students can calculate the area of different slices and use ratios to work out pricing for single slices. This helps them understand how algebra can be applied to real-world situations by relating the area and cost of individual slices to the whole pizza. 🍕➗💵
        """)

    # Conversions between measurements for ingredients
    with st.expander("Conversions for Ingredients - Fractions and Ratios 🍕🔢"):
        st.write("""
        Conversions between measurements for ingredients offer a practical way to work with fractions and ratios. For instance, students can calculate the conversion rate between units to figure out ingredient amounts in different quantities, making use of fractions and ratios to get accurate results. 🍕🔢
        """)

    # Combining fractions
    with st.expander("Combining Fractions for Pizza Slices 🍕➕🍕"):
        st.write("""
        Combining fractions can be visualized by adding slices from different pizzas. Students can add the number of slices from two pizzas and work out the total cost, providing a real-life application of fraction addition. 🍕➕🍕
        """)

    # Backwards ratios
    with st.expander("Backwards Ratios with Algebra 🔄🍕"):
        st.write("""
        Backwards ratios involve finding a part from a whole number using algebra. For example, if a whole pizza’s value is known, students can use algebra to calculate the portion (or slice) they need, making it a practical introduction to working with ratios in reverse. 🔄🍕
        """)

    # Combining ratios
    with st.expander("Combining Ratios for Different Ingredients 🍕🥄"):
        st.write("""
        By combining ratios, students can calculate the proportional amounts of different ingredients required for a pizza recipe. This demonstrates the use of ratios to maintain consistency in recipes and helps students understand how ratios can be combined for complex calculations. 🍕🥄
        """)

    # Using ratios to determine pizza portions based on spend
    with st.expander("Using Ratios for Spending and Pizza Portions 🍕💵"):
        st.write("""
        Ratios can help determine pizza portions based on spend. For example, if two people pay a total of £10 (one paying £4 and the other £6), students can divide the pizza in proportion to the amount each person paid, which introduces the concept of equitable distribution using ratios. 🍕💵
        """)

    # Turning customer orders into ratios
    with st.expander("Turning Customer Orders into Ratios 🍕📊"):
        st.write("""
        Customer orders can be turned into ratios to fulfill specific ingredient requests. For example, a customer may ask for a pizza with half as many tomatoes as onions. Students can use ratios to calculate ingredient quantities based on this request, giving them a real-world application of ratio calculations. 🍕📊
        """)

    # Ingredient ratios for different pizzas 🍕➗
    with st.expander("Calculating Ratios for Different Pizzas 🍕🍴"):
        st.write("""
        Using ratios, students can determine how many pizzas of each type can be made from given ingredient amounts. For instance, if they have enough ingredients to make four times as many of one type as another, they can calculate the total number of pizzas that can be prepared. 🍕📊
        """)

    # Working out percentages for tips and profits 💵🍕
    with st.expander("Percentages for Tips and Profit Calculation 💸🍕"):
        st.write("""
        Percentages are used to work out tips and calculate profits. Students can calculate the tip as a percentage of the total bill or compare the cost of making a pizza with its selling price to determine profit margins. This offers practical application of percentage calculations in a real-life business context. 🍕💰
        """)

# Choice of Topic 🎮🍕🧑‍🏫
with tab3:
    st.title('Choice of Topic 🎮🍕')
    st.subheader("Ranking of ideas 🏆")
    st.write("""
    Based on our broad and specific research, including insights from examiner reports and topics that link well to VR (such as ratio expansions), we have ranked the following ideas in terms of priority.
    Our rankings are based on the time and effort required to incorporate each idea, as well as the potential benefit each can bring to the user. The ideas are listed below in order of priority: 
    """)
    
    # 1. Area of circle, pizza inside pizza box 🍕🔵
    with st.expander("1 - Area of Circle: Pizza Inside Pizza Box 🍕📦"):
        st.write("""
        In this VR scenario, students can explore the area of a circle with a pizza inside a pizza box. Given the area, they could calculate the diameter, explore segments of a circle, and see real-world applications of circular geometry. This topic is highly engaging and immediately relevant to the concept of pizza, making it our top priority. 🍕🔵
        """)

    # 2. Tills and transactions 💳
    with st.expander("2 - Tills and Transactions: Working Out Change or Tips 💸🧾"):
        st.write("""
        This topic allows students to work with basic operations involving money, such as calculating change, percentage tips, and determining how many pizzas can be bought within a certain budget. Extending this idea, students could calculate profits over time, creating practical applications for finance skills. 💳🍕
        """)

    # 3. Ratios and Conversions ➗🍕
    with st.expander("3 - Ratios and Conversions 🍕🔢"):
        st.write("""
        Students can learn to work with ratios and conversions, such as figuring out ratios from word problems and converting between measurement units. This topic also ties into fractional understanding within ratios, making it highly beneficial for mathematical reasoning. 🔢🍕
        """)

    # 4. 3D Shapes and Volumes 🧀📦
    with st.expander("4 - 3D Shapes and Volumes 📦🍕"):
        st.write("""
        This idea explores 3D shapes, such as calculating how many pizzas can fit inside an oven or understanding front and side elevations as extensions of area problems. Additionally, students can learn about angles around a point by splitting pizzas into slices, adding to their spatial and geometric reasoning skills. 🍕🔲
        """)

    # 5. Triangular and Other Shaped Pizzas 🍕🔺
    with st.expander("5 - Triangular Pizzas and Other Shapes 🍕🔺"):
        st.write("""
        This activity could introduce students to different shapes, like triangular pizzas, extending their understanding of area and perimeter with unconventional pizza shapes, helping them appreciate the diversity of geometric forms. 🍕🔺
        """)

    # 6. Hypothetical Situations 🔮🍕
    with st.expander("6 - Hypothetical Situations: Oven Size Changes 🔮🍕"):
        st.write("""
        In hypothetical scenarios, students could use fractions and scaling concepts to answer questions like “If the oven were twice as big, how many pizzas could fit?” This encourages flexible thinking and real-world applications of math. 🔮🍕
        """)

    # 7. Functional Comparison for Utilities ⚡🍕
    with st.expander("7 - Comparing Functions for Utility Bills ⚡🍕"):
        st.write("""
        This topic involves comparing utility costs from different companies, such as Company A offering power at a rate f(x) and Company B at f(y). Students can work out which company is more cost-effective, learning about functions in the context of utility bills. ⚡🍕
        """)

    # 8. Franchising and Business Expansion 🍕🏢
    with st.expander("8 - Franchising and Business Expansion 🍕🏢"):
        st.write("""
        A VR scenario about franchising a restaurant could introduce concepts such as delivery services and operational expansions, providing students with insights into business math and logistics. 🍕🏢
        """)

    st.subheader("The top three concepts 🌟")

    # 1. Area of Circle and Related Concepts 🔵🍕
    with st.expander("1 - Area of Circle and Related Geometry: Pizza Inside Pizza Box 🍕📦"):
        st.write("""
        In this VR concept, students can explore the area of a circle with practical pizza-related examples:
        
        - **Basic Calculations**: Given the area, students can calculate the diameter of a pizza or explore circle segments.
        - **Extensions into 3D Shapes and Volume**: Students can calculate how many pizzas fit inside an oven or analyze front and side elevations as visual extensions of area concepts. Angles around a point can also be demonstrated by slicing a pizza, helping students grasp angle calculations in a tangible way.
        - **Area Calculations and Variations**: Students can work out the area from the radius or diameter, or work backward from the area to find the radius, reinforcing the connection between area and radius. Additional exercises, like determining if a pizza fits in a box or calculating the crust-to-pizza ratio with circles within circles, offer further depth to this concept. 🍕🔵
        """)

    # 2. Tills and Transactions 💳🍕
    with st.expander("2 - Tills and Transactions: Working Out Change and Tips 💸🍕"):
        st.write("""
        This topic uses realistic cash register (till) scenarios to teach money-related math skills:
        
        - **Money Operations**: Students learn to calculate change, figure out percentage tips, and determine how many pizzas can be bought within a set budget. This introduces essential finance skills in a familiar context. 💳🍕
        - **Profit-Time Graphs**: As an extension, students can calculate profits over time, such as through profit-time graphs. Additionally, they could work on determining salaries, hourly pay rates, and decide if employees should get a bonus based on tips received. 💸📊
        - **Menu-Based Exercises**: By using a virtual menu, students can practice giving answers in terms of pence or pounds, calculate change, and figure out what they can afford with a set amount of money or how much change they would receive after making purchases. 🍕🍴
        """)

    # 3. Ratios, Fractions, and Conversions ➗🍕
    with st.expander("3 - Ratios, Fractions, and Conversions 🍕🔢"):
        st.write("""
        This topic allows students to explore ratios and conversions through practical, pizza-based examples:

        - **Word Problems and Ratios**: Students practice working out ratios from worded questions, using real-world scenarios such as ingredient quantities in recipes or pizza proportions. ➗🍕
        - **Conversions Between Measurements**: Exercises include converting between units for measurements, enhancing their understanding of real-life applications of ratios and fractions. 🍕📏
        - **Algebra in Ratios**: Introducing algebra, students can solve ratio problems that include unknowns, reinforcing their algebraic reasoning within a practical context. 🍕🔢
        """)

    st.subheader("Our final decision 🎮🍕")
    st.write("""
        The reason we chose circles as a final topic:

        - **Easily integrable into the game**: Pizzas are usually circles, and customers can require specific areas/segment pizzas, etc. Customers could require a takeaway box, and hence the diameter of the pizza would need to be known in order to find the right pizza box size. 🍕🎮
        - **Link to syllabus**: Links to the majority of GCSE sub-sections taken from the GCSE syllabus. 🎓
        - **Adaptable**: Easily adaptable levels to challenge different users' abilities in math – can have foundation questions all the way up to a grade 9 style question for students reaching the highest levels. 🍕🎮
        """)
