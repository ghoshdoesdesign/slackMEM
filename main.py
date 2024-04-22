import streamlit as st
# st.set_page_config(page_title="Hustler AI",
#                    page_icon=":bridge_at_night:",
#                    layout="wide")


st.image("big_02.jpg")

# with open( "app\style.css" ) as css:
#     st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)



tab1, tab2, tab3 = st.tabs(["About", "Startups", "HustlerAI"])
#st.image("cover_image_10.jpg")

css = '''
<style>
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size:1.2rem;
    }
</style>
'''

st.markdown(css, unsafe_allow_html=True)

with tab1:

    st.image("about_pt1_05.jpg")
    st.image("about_pt2_04.jpg")

    col1, col2, col3 , col4, col5 = st.columns(5)

    with col1:
        pass
    with col2:
        pass
    with col4:
        pass
    with col5:
        pass
    with col3 :
        
        center_button = st.link_button("Feedback!", "https://forms.gle/gqeDsSN4jYxLAwiV9")


    st.image("disc_02.jpg")



    #st.image("cover_image_10.jpg")

with tab2:
    #st.image("cover_image_10.jpg")
    st.write("**Name**: [Leap AI](https://www.tryleap.ai/)")
    st.write("**Funding**: 1.4M, Seed")
    st.write("**Industry**: Artificial Intelligence, B2B Software")
    intro_text = """
    Leap AI is a no-code AI platform that allows users to create custom AI-powered automations and workflows without coding expertise, 
    leveraging integrations with leading AI providers to streamline a wide range of business processes and enhance productivity.
        """
    st.write(f'<p style="color:#68696b">{intro_text}</p>', unsafe_allow_html=True)
    st.write("**Probable folks to connect with**:")
    st.write("[Alex Schachne](https://www.linkedin.com/in/alexschachne/): Co-Founder, [Mariano Fuentes](https://www.linkedin.com/in/marianofuentesdev/): Founding Engineer, [Claudio Fuentes](https://www.linkedin.com/in/claudiofuen/): Co-Founder & CEO")

    #st.divider()
    st.image("red_divider_2.jpg")



    st.write("**Name**: [Audioshake](https://www.audioshake.ai/)")
    st.write("**Funding**: 1.4M, Seed")
    st.write("**Industry**: Audio, Music, Artificial Intelligence, B2B Software")
    intro_text = """
    AudioShake is an AI-powered platform that can separate audio recordings into their component parts and stems, enabling a wide range
    of applications like music remixing, audio editing, localization, and interactive audio experiences. The technology has been praised 
    for its high quality and accuracy, and used by major music labels, film studios, artists, and app developers to make audio more interactive, customizable, and 
    accessible."""
    st.write(f'<p style="color:#68696b">{intro_text}</p>', unsafe_allow_html=True)
    st.write("**Probable folks to connect with**:")
    st.write("[Jonathan Lott](https://www.linkedin.com/in/jlott1/): Engineering Director, [Ibrahim Conteh](https://www.linkedin.com/in/ibrahim-conteh-42a518b2/): Software Engineer, [April Anderson](https://www.linkedin.com/in/apriland/): Marketing and Operations")

    st.image("red_divider_2.jpg")



    st.write("**Name**: [Celestial AI](https://www.celestial.ai/)")
    st.write("**Funding**: 175M, Series C")
    st.write("**Industry**: Artificial Intelligence, Computing, Semiconductors")
    intro_text = """
    Celestial AI has developed the Photonic Fabric, an optical interconnect technology platform that enables the disaggregation of 
    compute and memory in data centers. This breakthrough technology is claimed to deliver over 25x greater bandwidth and memory 
    capacity while reducing latency and power consumption, addressing the growing challenges of hyperscale data centers. Celestial AI
    is working on large-scale customer collaborations to commercialize and scale the adoption of its Photonic Fabric technology to power the next generation of high-performance computing and AI applications."""
    st.write(f'<p style="color:#68696b">{intro_text}</p>', unsafe_allow_html=True)
    st.write("**Probable folks to connect with**:")
    st.write("[Santhosh Narayana](https://www.linkedin.com/in/san-nar/): Senior Hardware Engineer, [Jonathan Sparling](https://www.linkedin.com/in/jonathan-sparling-26176a129/): Machine Learning Lead, [Kurtis Park](https://www.linkedin.com/in/kurtispark/): Head of Global Talent")

    st.image("red_divider_2.jpg")




    st.write("**Name**: [Clerk](https://www.clerk.com)")
    st.write("**Funding**: 30M, Series B")
    st.write("**Industry**: Cloud Computing, B2B Software")
    intro_text = """
    Clerk.com provides a complete suite of embeddable user interface components, flexible APIs, and admin dashboards to help businesses 
    authenticate and manage their users. The platform offers features like pixel-perfect UI components, social sign-on, fraud detection, 
    and multi-factor authentication, all while being SOC 2 certified and CCPA compliant.
        """
    st.write(f'<p style="color:#68696b">{intro_text}</p>', unsafe_allow_html=True)
    st.write("**Probable folks to connect with**:")
    st.write("[Kyle MacDonald](https://www.linkedin.com/in/macdonaldky/): Head of Product, [Rodney Urquhart](https://www.linkedin.com/in/rodneyu215/): Head of Developer Success, [Tom Milewski](https://www.linkedin.com/in/tmilewski/): Senior Software Engineer")

    st.image("red_divider_2.jpg")




    st.write("**Name**: [Rune Labs](https://www.runelabs.io/)")
    st.write("**Funding**: 12M, Series Unknown")
    st.write("**Industry**: Bio Sciences, Data, Analytics, B2B Software")
    intro_text = """
    At Rune Labs, our mission revolves around harnessing clinical brain data to foster meaningful impact, always mindful of the individuals 
    behind the data. Empathy is at our core, particularly for those grappling with brain disorders and the dedicated clinicians and researchers 
    supporting them. This human-centered perspective permeates our company culture, emphasizing integrity and empathy in all our endeavors.
        """
    st.write(f'<p style="color:#68696b">{intro_text}</p>', unsafe_allow_html=True)
    st.write("**Probable folks to connect with**:")
    st.write("[Patrick Mutuku](https://www.linkedin.com/in/patrickmutuku/): Software Engineer, [Witney Chen](https://www.linkedin.com/in/witney-chen/): Lead Neuroscientist / Data Scientist at Rune Labs, [Girish Nanda](https://www.linkedin.com/in/girishnanda/): Principal Software Engineer")

    st.image("red_divider_2.jpg")





    st.write("**Name**: [Better Stack](https://betterstack.com/?utm_medium=c&utm_campaign=adwords15371474121&utm_source=adwords&utm_content=564382922529&utm_term=betterstack&gad_source=1&gclid=Cj0KCQjwk6SwBhDPARIsAJ59Gwfr0-8vLkY69s6fg1vGhY3jmoKD2tMxU-cUd3SyOyMCBBWie_pZtJ8aAqggEALw_wcB)")
    st.write("**Funding**: 10M, Series Unknown")
    st.write("**Industry**: Cloud Computing, B2B Software")
    intro_text = """
    Betterstack.com provides a unified platform that helps developers and teams spot, resolve, and prevent downtime across their entire technology
    stack. The platform offers features like real-time monitoring, centralized logging and querying, incident management, and customizable dashboards. 
    It is trusted by engineering teams around the world to simplify their observability and incident response workflows.
    """
    st.write(f'<p style="color:#68696b">{intro_text}</p>', unsafe_allow_html=True)
    st.write("**Probable folks to connect with**:")
    st.write("[Veronika Kolejak](https://www.linkedin.com/in/veronikakolejak/): Co-Founder, [William Tatarko](https://www.linkedin.com/in/william-tatarko-83081215b/): Software Engineer, [Juraj Masar](https://www.linkedin.com/in/masarjuraj/): Product Designer")

    st.image("red_divider_2.jpg")




    st.write("**Name**: [Recogni](https://www.recogni.com/)")
    st.write("**Funding**: 102M, Series C")
    st.write("**Industry**: Autonomous Vehicles, Artificial Intelligence, Semiconductor")
    intro_text = """
    Recogni develops AI-based inference processing solutions that provide unprecedented performance, scalability, and power efficiency for
    applications like autonomous vehicles and generative AI. The company's flagship product, Scorpio, is a low-power AI compute solution 
    capable of 1 Peta-FLOP of inference processing, addressing the growing compute demands of advanced AI models.
    """
    st.write(f'<p style="color:#68696b">{intro_text}</p>', unsafe_allow_html=True)
    st.write("**Probable folks to connect with**:")
    st.write("[Kalyana S Venkataraman](https://www.linkedin.com/in/kalyanasv/): Design Engineer, [Berend Ozceri](https://www.linkedin.com/in/berend-ozceri-993650/): VP of Engineering, [Sidhart Krishnamurthi](https://www.linkedin.com/in/sidhart-krishnamurthi/): Product Manager")

    st.image("red_divider_2.jpg")



    st.write("**Name**: [Forta Health](https://www.fortahealth.com)")
    st.write("**Funding**: 55M, Series A")
    st.write("**Industry**: Family, Healthcare, B2B Software")
    intro_text = """
    Forta Health is an AI healthcare company improving access to quality autism therapy. They empower parents to provide applied 
    behavior analysis (ABA) therapy to their children with autism, providing training, support, and compensation. Forta plans to expand its family-powered 
    model and continue AI research to enhance care delivery.
    """
    st.write(f'<p style="color:#68696b">{intro_text}</p>', unsafe_allow_html=True)
    st.write("**Probable folks to connect with**:")
    st.write("[Jiwon Shin](https://www.linkedin.com/in/jiwonej/): Data Analyst, [Navan Singh](https://www.linkedin.com/in/navan-singh/): Senior Software Engineer, [Meg L.](https://www.linkedin.com/in/meg-lowe92/): Design Lead")

    st.image("red_divider_2.jpg")



    st.write("**Name**: [BuildClub](https://www.buildclub.com)")
    st.write("**Funding**: 1.2M, Series A")
    st.write("**Industry**: E-Commerce, Material Sourcing, B2B Software")
    intro_text = """
    BuildClub contractors a single portal to find the most cost-effective materials closest to their job sites. The BuildClub solves 
    the market problem of getting the right building materials, on the job site, at the right time. We eliminate the need for carpenters, 
    plumbers, electricians, building maintenance, and other trades to get in their trucks tobuy materials during the workday, making them highly inefficient.
    """
    st.write(f'<p style="color:#68696b">{intro_text}</p>', unsafe_allow_html=True)
    st.write("**Probable folks to connect with**:")
    st.write("[Stephen Forte](https://www.linkedin.com/in/forte/): Founder and CEO, [Pavel Kirakosyan](https://www.linkedin.com/in/pkirakosyan/): Director of Engineering")
    
    st.image("red_divider_2.jpg")






    st.write("**Name**: [Recraft AI](https://www.recraft.ai/)")
    st.write("**Funding**: 12M, Series A")
    st.write("**Industry**: Artificial Intelligence, 3D, B2B Software")
    intro_text = """
    Recraft, a leader in AI and 3D technology, secured $12 million in Series A funding to advance innovative B2B solutions. 
    Their flagship AI-powered 3D design platform accelerates product development, while specialized tools automate tasks in
    various industries. With a focus on collaboration and innovation, Recraft aims to redefine problem-solving and decision-making,
    positioning itself as a trusted partner for businesses seeking transformative technology solutions.
        """
    st.write(f'<p style="color:#68696b">{intro_text}</p>', unsafe_allow_html=True)
    st.write("**Probable folks to connect with**:")
    st.write("[Danila Baigushev](https://www.linkedin.com/in/danila-baigushev-290080234/): Machine Learning Researcher, [Daniil Anastasyev](https://www.linkedin.com/in/daniil-anastasyev/): Senior Machine Learning Engineer")

    st.image("red_divider_2.jpg")



    st.write("**Name**: [Campfire](https://meetcampfire.com)")
    st.write("**Funding**: 3.5M, Seed")
    st.write("**Industry**: Accounting, Finance, B2B Software")
    intro_text = """
    Campfire is the modern accounting platform for startups and mid-size tech companies, offering a powerful general ledger, invoicing, billing,
    revenue accounting and reporting, financial statements, AI-powered conversational reporting, and automated accounting workflows. Campfire is
    a modern replacement for legacy, small business accounting software and mid-market ERPs."""

    st.write(f'<p style="color:#68696b">{intro_text}</p>', unsafe_allow_html=True)
    st.write("**Probable folks to connect with**:")
    st.write("[John Glasgow](https://www.linkedin.com/in/johnglasgow/): CEO, [Fernando San Martin](https://www.linkedin.com/in/fsanmartinjorquera/):CTO, [Daniel Lantz](https://www.linkedin.com/in/dflantz/): Software Engineer")

    st.image("red_divider_2.jpg")




    st.write("**Name**: [GALY](https://www.galy.co)")
    st.write("**Funding**: 20.1M, Venture - Series Unknown")
    st.write("**Industry**: Agriculture")
    intro_text = """ GALY is a developer of cellular agriculture using biotechnology and sustainable, less energy-land-intensive methods to
    produce natural products. The company creates cotton in a laboratory context from cells utilizing a proprietary method that is faster,
    higher quality, and cheaper than natural cotton, with a drastically lower environmental impact. GALY's cell-culture platform can be
    applied to produce products beyond cotton, and the company has raised over $32 million to date from investors including John Doerr,
    Sergey Brin, and others."""

    st.write(f'<p style="color:#68696b">{intro_text}</p>', unsafe_allow_html=True)
    st.write("**Probable folks to connect with**:")
    st.write("[Luciano Bueno](https://www.linkedin.com/in/luciano-bueno/): CEO, [David Dodds](https://www.linkedin.com/in/techdiligence/):CTO, [Luis Alvear Tesouro](https://www.linkedin.com/in/luis-alvear/): Software Engineer")

    st.image("red_divider_2.jpg")





    st.write("**Name**: [Abstract Security](https://www.abstract.security)")
    st.write("**Funding**: 8.5M, Seed")
    st.write("**Industry**: Artificial Intelligence, Analytics, Security, B2B Software")
    intro_text = """
    Abstract Security has created a revolutionary platform, equipped with an AI-powered assistant, to better centralize the management of security analytics.
    Abstract transcends next-gen SIEM solutions by correlating data in real-time between data streams. As a result, compliance and security data can
    be leveraged separately to increase detection effectiveness and lower costs."""
    st.write(f'<p style="color:#68696b">{intro_text}</p>', unsafe_allow_html=True)
    st.write("**Probable folks to connect with**:")
    st.write("[Colby DeRodeff](https://www.linkedin.com/in/colbyderodeff/): CEO, [Stephen Iota](https://www.linkedin.com/in/iota/): Software Engineer, [Seokjoo Yoo](https://www.linkedin.com/in/seokjoo-yoo/): Software Engineer")

    st.image("red_divider_2.jpg")


    st.write("**Name**: [Parspec](https://parspec.io)")
    st.write("**Funding**: 11.5M, Seed")
    st.write("**Industry**: Artificial Intelligence, B2B Software")

    intro_text = """
    We are a technology company utilizing AI to serve the supply chain for the building and construction industry. Our mission
    is to simplify the process of discovering and sourcing the best available construction products and materials. The platform we're
    building empowers our customers, and the construction industry in general, to build and operate the facilities and infrastructure that
    our economy depends on more efficiently; and to reduce the significant impact these structures have on our natural environment."""
    st.write(f'<p style="color:#68696b">{intro_text}</p>', unsafe_allow_html=True)
    st.write("**Probable folks to connect with**:")
    st.write("[Abhijit Mitra](https://www.linkedin.com/in/abhijit-mitra-a238ab13b/): Lead Frontend Engineer, [Jenna Nicholls](https://www.linkedin.com/in/jenna-nicholls19/): Sr User Experience Designer, [Ben Kanellitsas](https://www.linkedin.com/in/benkanellitsas/): Head of Operations")

    st.image("red_divider_2.jpg")




    st.write("**Name**: [Fieldguide](https://www.fieldguide.io)")
    st.write("**Funding**: 30M, Series B")
    st.write("**Industry**: Artificial Intelligence, B2B Software")

    intro_text = """
    Fieldguide offers market-leading Artificial Intelligence that helps Advisory and Audit firms grow. AI platform digitizes the end-to-end engagement
    lifecycle — delivering dramatically better results to professionals and their clients. Fieldguide is trusted by top CPA and consulting firms
    to unlock growth, increase margins, and delight clients."""
    st.write(f'<p style="color:#68696b">{intro_text}</p>', unsafe_allow_html=True)
    st.write("**Probable folks to connect with**:")
    st.write("[Nishant Panchal](https://www.linkedin.com/in/nishant-panchal/): Design Lead, [Natalie Amend](https://www.linkedin.com/in/natalieamend/): Recruiting Lead, [Ishvaraus Davis](https://www.linkedin.com/in/ishvarausdavis/): Senior Software Engineering Manager")

    st.image("red_divider_2.jpg")








    st.write("**Name**: [Abstract](https://abstract.us)")
    st.write("**Funding**: 4.2M, Seed")
    st.write("**Industry**: Artificial Intelligence, B2B Software")

    intro_text = """
    Abstract is a VC-backed applied AI-tech startup operating in the Gov & Legal sectors. Abstract is a project management & intelligence platform
    for understanding the impact of government policies on business and communities, as well as a tool to help improve those policies. Abstract
    leverages AI models, and proprietary data processing tech, to uncover risk & opportunity that current & changing government policy poses for
    an organizations product, assets, investments, labor-force, manufacturing, etc…"""
    st.write(f'<p style="color:#68696b">{intro_text}</p>', unsafe_allow_html=True)
    st.write("**Probable folks to connect with**:")
    st.write("[Neal Patel](https://www.linkedin.com/in/nealpareshpatel/): Data Engineering, [Tyler K.](https://www.linkedin.com/in/tylerkneidl/): Full Stack Engineer, [Patricio Utz](https://www.linkedin.com/in/patrick-utz/): Patricio Utz")

    st.image("red_divider_2.jpg")






    st.write("**Name**: [Lumino](https://www.luminolabs.ai)")
    st.write("**Funding**: 2.8M, Pre-Seed")
    st.write("**Industry**: Artificial Intelligence, B2B Software")

    intro_text = """
    Decentralized compute protocol to train and fine-tune AI models"""
    st.write(f'<p style="color:#68696b">{intro_text}</p>', unsafe_allow_html=True)
    st.write("**Probable folks to connect with**:")
    st.write("[Eshan Chordia](https://www.linkedin.com/in/echordia/): Co-Founder, [Yogesh Darji](https://www.linkedin.com/in/yogeshdarji/): Co-Founder")

    st.image("red_divider_2.jpg")



    st.write("**Name**: [Activeloop](https://activeloop.ai)")
    st.write("**Funding**: 11M, Series A")
    st.write("**Industry**: Artificial Intelligence, B2B Software")

    intro_text = """
    Deep Lake is a Database for AI powered by a unique storage format optimized for deep-learning and Large Language Model (LLM)
    based applications. It simplifies the deployment of enterprise-grade LLM-based products by offering storage for all data types (embeddings, audio,
    text, videos, images, pdfs, annotations, etc.), querying and vector search, data streaming while training models at scale, data versioning and
    lineage for all workloads, and integrations with popular tools such as LangChain, LlamaIndex, Weights & Biases, and many more. Deep Lake
    works with data of any size, it is serverless, and it enables you to store all of your data in one place."""
    st.write(f'<p style="color:#68696b">{intro_text}</p>', unsafe_allow_html=True)
    st.write("**Probable folks to connect with**:")
    st.write("[Joseph Ismailyan](https://www.linkedin.com/in/joseph-ismailyan/): Senior Software Engineer, [Taylor Stubbs](https://www.linkedin.com/in/stubbscommataylor/): Senior Software Engineer, [Mikayel H](https://www.linkedin.com/in/mikayelharutyunyan/): Head of Marketing & Growth")

    st.image("red_divider_2.jpg")






    st.write("**Name**: [Cleric](https://cleric.io)")
    st.write("**Funding**: 4.3M, Seed")
    st.write("**Industry**: Artificial Intelligence, Cloud Computing")

    intro_text = """
    Cleric is an AI-powered agent designed to manage and resolve issues in production environments autonomously. It uses an LLM-based reasoning engine
    to react to, interpret, and implement solutions to production issues, even those it's encountering for the first time. They envision a future
    where engineers can concentrate on software development while Cleric takes care of the production environment. Their mission is to develop autonomous
    software that can manage, repair and optimize itself."""
    st.write(f'<p style="color:#68696b">{intro_text}</p>', unsafe_allow_html=True)
    st.write("**Probable folks to connect with**:")
    st.write("[Shahram Anver](https://www.linkedin.com/in/shahramanver/): CEO, [Willem Pienaar](https://www.linkedin.com/in/willempienaar/): CTO, [Peter Richens](https://www.linkedin.com/in/peter-richens/): Principal Engineer")

    st.image("red_divider_2.jpg")





    st.write("*Name*: [Ambience Healthcare](https://www.ambiencehealthcare.com/)")
    st.write("*Funding*: $7M")
    st.write("*Industry*: Artificial Intelligence, Healthcare, B2B Software")

    intro_text = """
    Ambience Healthcare’s mission is to supercharge clinicians with breakthrough generative AI technology. The Ambience AI operating system consists of a holistic
    suite of applications, designed to alleviate clinician burnout, improve overall system efficiency, and enable high-quality care. By partnering with Ambience,
    healthcare systems reduce documentation time by an average of 78%, improve coding integrity, and achieve at least a 5X return on investment."""
    st.write(f'<p style="color:#68696b">{intro_text}</p>', unsafe_allow_html=True)
    st.write("*Probable folks to connect with*:")
    st.write("[Brendan Fortuner](https://www.linkedin.com/in/bfortuner/): Head of Engineering, [Nikhil Buduma](https://www.linkedin.com/in/nikhilbuduma/): Co-Founder & Chief Scientist, [Tian Dou](https://www.linkedin.com/in/tian-dou/): Product Design")

    st.image("red_divider_2.jpg")




    st.write("*Name*: [OpenPipe](https://openpipe.ai/)")
    st.write("*Funding*: $6.7M seed")
    st.write("*Industry*: Data, Artificial Intelligence, B2B Software")

    intro_text = """
    Fine-tune models to replace your LLM prompts. It automatically convert expensive LLM prompts into fast, cheap fine-tuned models."""
    st.write(f'<p style="color:#68696b">{intro_text}</p>', unsafe_allow_html=True)
    st.write("*Probable folks to connect with*:")
    st.write("[Kyle Corbitt](https://www.linkedin.com/in/kcorbitt/): Co-Founder, [David Corbitt](https://www.linkedin.com/in/davidcorbitt/): Co-Founder, [Bohdan Kovalevskyi](https://www.linkedin.com/in/bohdan-kovalevskyi/): Full Stack Developer")

    st.image("red_divider_2.jpg")



    st.write("*Name*: [Cognition](http://www.cognition-labs.com/)")
    st.write("*Funding*: $21M Series A")
    st.write("*Industry*: Artificial Intelligence, Cloud Computing, Computer Engineering, B2B Software")

    intro_text = """
    Makers of Devin, the first AI software engineer. They are an applied AI lab focused on reasoning.
    They’re building AI teammates with capabilities far beyond today’s existing AI tools. By solving reasoning, they can unlock new possibilities in a wide range of disciplines—code is just the beginning."""
    st.write(f'<p style="color:#68696b">{intro_text}</p>', unsafe_allow_html=True)
    st.write("*Probable folks to connect with*:")
    st.write("[Walden Yan](https://www.linkedin.com/in/waldenyan/): Co-Founder, [Andrew H.](https://www.linkedin.com/in/andrew-he/): Human Software Engineer, [Sara Xiang](https://www.linkedin.com/in/saraxiang/): Human Product Manager")

    st.image("red_divider_2.jpg")


























with tab3:
    #st.image("cover_image_10.jpg")
    import pip
    import numpy as np
    import pandas as pd
    import streamlit as st


    from langchain.agents import AgentType, Tool, initialize_agent
    from langchain.chains import LLMMathChain
    from langchain.chat_models import ChatOpenAI
    from langchain.utilities import SerpAPIWrapper, SQLDatabase
    #from langchain_experimental.sql import SQLDatabaseChain

    from dotenv import load_dotenv


    def configure():
        load_dotenv()

    

    import os
    configure()
    os.environ['OPENAI_API_KEY'] = "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"
    os.environ['SERPAPI_API_KEY'] = "181c6aacc8075e235ee567884f58f298dc35033b6de749ab6537f4b7cd1655f2"
    
    np.random.seed(0)




    # %%
    import sklearn


    #if st.button("Ask Yoda"):

    llm = ChatOpenAI(temperature=0, model="gpt-4-turbo-preview")
    search = SerpAPIWrapper()
    llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)
    # db = SQLDatabase.from_uri("sqlite:///../../../../../notebooks/Chinook.db")
    # db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)
    tools = [
        Tool(
            name="Search",
            func=search.run,
            description="useful for when you need to answer questions about current events. You should ask targeted questions",
        ),
        Tool(
            name="Calculator",
            func=llm_math_chain.run,
            description="useful for when you need to answer questions about math",
        ),
        
    ]


    system_prompt = st.text_input("Please enter your story")
    company_input = st.text_input("Please enter the URL of the company you want to generate a blurb for: ")
    sample_output = "Hi X, I hope you're doing great.I'm a product designer with a master's in Design from UC Berkeley. Over the past 6 months, I've been working on building a platform for providing better economic opportunities for small businesses in India, particularly in the crafts sector. At the same time, I've had the opportunity to work as a Product Designer at companies like Ripple and Amadeus, where I gained valuable experience in building automation tools and streamlining workflows.Now, I'm looking to combine these two areas of expertise to create truly impactful products and experiences for small businesses. That's why I'm really interested in the work at Homebase. As a leading provider of workforce management solutions for small businesses, I believe Homebase is uniquely positioned to understand the challenges these companies face and develop tools that can make a real difference. I feel I could learn a lot from your team's insights and experiences. Would you be willing to have a 30-minute information interview with me in the coming weeks? Thank you so much for your time and consideration. Sincerely, Kabeer"


    from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
    # prompt = ChatPromptTemplate.from_messages(
    #     [
    #         ("system", "You are a Career advisor specializing in tech jobs - here is a profile of a candidate with their introduction: I've been a Product Designer for over three years, building SaaS products and strategies for companies such as Ripple and Amadeus. I recently completed my master's in Emerging Technology Design at UC Berkeley, focusing on leveraging design and technology to create economic opportunities for underrepresented communities. While working for Ripple, I discovered a major pain point that was overlooked. Ripple users had to manually conduct reconciliation tasks that took a lot of time and were prone to errors. They had to retrieve data from multiple sources and put in a lot of time to customize it based on their needs. Plus it wasn't aligned to the market standards. As a result, a lot of financial transactions were lost,  the users were frustrated with the time-consuming process. My breakthrough came with designing a reporting flow that automated the entire ordeal. This one-stop solution brought transparency, streamlined the reconciliation process, and ensured comprehensive payment tracking by improving the operating time by around 80%.  In doing so, it turned a frustrating, labor-intensive task into a seamless, reliable process. My professional journey at Amadeus, where I led the design for B2B and SaaS tools utilized by help desks at Air Canada and Southwest, serving over 30,000 airline agents, has prepared me for the challenges and opportunities at Front. The automated workflows we developed significantly enhanced the user journey and reduced agent processing time by 10 minutes, translating to approximately a 66% improvement in efficiency. Now whatever company is mentioned in the user prompt please say how this candidate is an good fit for that company. "),
    #         ("user", "{input}"),
    #         MessagesPlaceholder(variable_name="agent_scratchpad"),
    #     ]
    # )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", f"You are a Career advisor specializing in tech jobs. Here is a profile of a candidate with their introduction: {system_prompt}Write how the candidate’s experience and abilities make them a good fit for the company: {company_input}. Please write it in first person, as if the candidate is typing the message. Make it as human and personalized as possible and sound formal. Do deep research into the company’s projects and articles about their work and relate how the candidate's abilities and experiences can contribute to the betterment of the company, do not just stick to the core mission of the company, go beyond that. Be specific and do extensive research on the company by searching the internet, mostly from their website and blog posts about the mentioned company. Make the message within 100 words. Write the message as if the candidate wishes to learn more about the company’s ethos and work in the process building a long lasting connection. Keep the tone and wordings very similar to the user story. Do not add unnecessary adjectives. This is a {sample_output} follow the exact same structure as the sample_output and be as honest and as less robotic as possible. Dont hallucinate."),
            ("user", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )

    from langchain.tools.render import format_tool_to_openai_function
    llm_with_tools = llm.bind(functions=[format_tool_to_openai_function(t) for t in tools])

    from langchain.agents.format_scratchpad import format_to_openai_function_messages
    from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser

    agent = (
        {
            "input": lambda x: x["input"],
            "agent_scratchpad": lambda x: format_to_openai_function_messages(
                x["intermediate_steps"]
            ),
        }
        | prompt
        | llm_with_tools
        | OpenAIFunctionsAgentOutputParser()
    )

    from langchain.agents import AgentExecutor

    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)


    import os 


    #user_input = input("Please enter your query")

    user_input = "Craft a story as to how this candidate's profile fit well with the mission of the company mentioned"

    col1, col2, col3 , col4, col5 = st.columns(5)

    with col1:
        pass
    with col2:
        pass
    with col4:
        pass
    with col5:
        pass
    with col3 :
        center_button = st.button('Generate')

        #st.button("Ask chatterbox")


    if center_button == True:

        p=agent_executor.invoke(
        {
            "input": user_input
        }
        )
        output_text = p["output"]
        #print(output_text)

        with st.container(height=600):          
            st.markdown(f'<h1 style="color:#ff4c4b;font-size:16px;">{output_text}</h1>', unsafe_allow_html=True)

    
