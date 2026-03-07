import streamlit as st
import time
import base64

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="My Portfolio", page_icon="🌌", layout="wide")

# --- MASTER CSS STYLING ---
custom_css = """
<style>
    /* Hide Streamlit elements but KEEP the sidebar arrow */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Import modern font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* --- CENTERED HERO SECTION CSS --- */
    .hero-container {
        text-align: center; /* Locks everything to the center */
        padding: 20px 0 50px 0;
        animation: fadeSlideUp 0.8s ease-out forwards;
    }
    
    .hero-image {
        width: 220px;
        height: 220px;
        border-radius: 50%; /* Makes the image a perfect circle */
        object-fit: cover;
        margin-bottom: 25px;
        border: 4px solid #3a3a55;
        transition: all 0.4s ease;
    }
    
    .hero-image:hover {
        transform: scale(1.05);
        border-color: #E94057;
        box-shadow: 0 10px 30px rgba(233, 64, 87, 0.4);
    }
    
    /* MASSIVE ANIMATED NAME */
    .hero-title {
        font-size: 6rem; /* Huge size! */
        font-weight: 900;
        background: -webkit-linear-gradient(45deg, #8A2387, #E94057, #F27121);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
        padding-bottom: 10px;
        display: inline-block;
        transition: all 0.4s ease;
        cursor: default;
    }
    
    /* HOVER COLOR CHANGE ANIMATION */
    .hero-title:hover {
        background: -webkit-linear-gradient(45deg, #00f2fe, #4facfe, #00f2fe); /* Changes to vibrant blue/cyan */
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        transform: scale(1.05); /* Pops out slightly */
    }
    
    .hero-subtitle {
        font-size: 1.8rem;
        font-weight: 400;
        color: #A0AEC0;
        margin-bottom: 25px;
    }
    
    .hero-text {
        font-size: 1.2rem;
        color: #f7f7f7;
        max-width: 850px;
        margin: 0 auto; /* Centers the paragraph block */
        line-height: 1.7;
    }

    /* --- MASSIVE ICONS, LEFT-ALIGNED & ANIMATED TITLES CSS --- */
    .vertical-card {
        width: 100%; 
        max-width: 1400px; 
        margin: 0 0 50px 0; 
        display: flex;
        align-items: center;
        text-align: left;
        padding: 50px; 
        background: linear-gradient(145deg, #1e1e2f, #2a2a40);
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        border: 1px solid #3a3a55;
        transition: transform 0.4s ease, box-shadow 0.4s ease;
        animation: fadeSlideUp 0.8s ease-out forwards;
    }
    
    .vertical-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 15px 35px rgba(255, 255, 255, 0.15);
    }
    
    .vertical-card .tech-img {
        width: 180px; 
        height: 180px;
        margin-right: 60px; 
        flex-shrink: 0; 
        transition: transform 0.4s ease;
    }
    .vertical-card:hover .tech-img {
        transform: scale(1.15) rotate(5deg); 
    }
    
    .vertical-text-content {
        flex-grow: 1;
    }
    
    /* BOLD, ANIMATED TEXT BASE */
    .animated-title {
        font-size: 3rem; 
        font-weight: 900; 
        font-family: 'Inter', sans-serif;
        margin-bottom: 10px;
        background-size: 200% auto;
        color: #fff;
        background-clip: text;
        text-fill-color: transparent;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shine 3s linear infinite; 
    }

    /* UNIQUE VIBRANT COLORS */
    .title-ai { background-image: linear-gradient(to right, #00f2fe 0%, #4facfe 50%, #00f2fe 100%); }
    .title-strategy { background-image: linear-gradient(to right, #f2709c 0%, #ff9472 50%, #f2709c 100%); }
    .title-video { background-image: linear-gradient(to right, #43e97b 0%, #38f9d7 50%, #43e97b 100%); }
    .title-design { background-image: linear-gradient(to right, #fa709a 0%, #fee140 50%, #fa709a 100%); }

    @keyframes shine { to { background-position: 200% center; } }
    @keyframes fadeSlideUp { 0% { opacity: 0; transform: translateY(30px); } 100% { opacity: 1; transform: translateY(0); } }

    .tech-brief {
        color: #f7f7f7;
        font-size: 1.3rem; 
        margin-bottom: 15px;
        font-family: 'Inter', sans-serif;
        font-style: italic;
    }

    .tech-text-item {
        color: #A0AEC0;
        font-size: 1.15rem; 
        font-family: 'Inter', sans-serif;
        display: inline-block;
        transition: color 0.3s ease;
    }
    .vertical-card:hover .tech-text-item { color: #ffffff; }

    /* --- SIDEBAR CUSTOM NAVIGATION CSS --- */
    .stRadio div[role="radiogroup"] > label > div:first-child { display: none !important; }
    .stRadio div[role="radiogroup"] > label {
        background: rgba(30, 30, 47, 0.4);
        border: 1px solid #3a3a55;
        border-radius: 12px;
        padding: 15px 15px 15px 60px !important; 
        margin-bottom: 10px;
        position: relative;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .stRadio div[role="radiogroup"] > label:hover {
        transform: scale(1.05) translateX(5px);
        background: linear-gradient(145deg, #1e1e2f, #2a2a40);
        border-color: #E94057;
    }
    .stRadio div[role="radiogroup"] > label p {
        font-family: 'Inter', sans-serif;
        font-size: 1.05rem !important;
        color: #A0AEC0;
        transition: all 0.3s ease;
    }
    .stRadio div[role="radiogroup"] > label:hover p {
        font-weight: 900 !important;
        color: #ffffff !important;
    }
    .stRadio div[role="radiogroup"] > label::before {
        content: ''; position: absolute; left: 15px; top: 50%; transform: translateY(-50%);
        width: 30px; height: 30px; background-size: contain; background-repeat: no-repeat; transition: transform 0.3s ease;
    }
    .stRadio div[role="radiogroup"] > label:hover::before { transform: translateY(-50%) scale(1.2) rotate(5deg); }

    /* Assigning Sidebar Icons */
    .stRadio div[role="radiogroup"] > label:nth-child(1)::before { background-image: url('https://cdn-icons-png.flaticon.com/512/1946/1946488.png'); }
    .stRadio div[role="radiogroup"] > label:nth-child(2)::before { background-image: url('https://cdn-icons-png.flaticon.com/512/2083/2083213.png'); }
    .stRadio div[role="radiogroup"] > label:nth-child(3)::before { background-image: url('https://cdn-icons-png.flaticon.com/512/3112/3112521.png'); }
    .stRadio div[role="radiogroup"] > label:nth-child(4)::before { background-image: url('https://cdn-icons-png.flaticon.com/512/4712/4712035.png'); }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("Navigation")
    
    # PERFECTLY MATCHED PAGE NAMES (No Emojis!)
    page = st.radio("Menu", [
        "Home", 
        "AI & Prompt Engineering", 
        "Video Editing", 
        "Chat with My AI Clone"
    ], label_visibility="collapsed")
    
    # --- UPGRADED ANIMATED CONNECT SECTION ---
    st.markdown("""
    <style>
        .social-link {
            display: flex;
            align-items: center;
            text-decoration: none;
            padding: 10px 15px;
            margin-bottom: 12px;
            background: rgba(30, 30, 47, 0.4);
            border: 1px solid #3a3a55;
            border-radius: 10px;
            color: #A0AEC0 !important;
            font-family: 'Inter', sans-serif;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        .social-link img {
            width: 24px;
            height: 24px;
            margin-right: 15px;
            transition: transform 0.3s ease;
        }
        .social-link:hover {
            background: linear-gradient(145deg, #1e1e2f, #2a2a40);
            border-color: #E94057;
            transform: translateX(8px);
            color: #ffffff !important;
            box-shadow: 0 4px 15px rgba(233, 64, 87, 0.3);
        }
        .social-link:hover img {
            transform: scale(1.2) rotate(10deg);
        }
        
        /* Vibrant Glowing Resume Button */
        .download-btn {
            display: block;
            text-align: center;
            text-decoration: none;
            background: linear-gradient(45deg, #8A2387, #E94057, #F27121);
            color: white !important;
            padding: 12px;
            border-radius: 25px;
            font-family: 'Inter', sans-serif;
            font-weight: 800;
            font-size: 1.05rem;
            margin-top: 20px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(233, 64, 87, 0.4);
            border: 2px solid transparent;
        }
        .download-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(233, 64, 87, 0.7);
            border-color: rgba(255,255,255,0.5);
        }
        
        .connect-title {
            color: #ffffff;
            font-family: 'Inter', sans-serif;
            font-weight: 800;
            font-size: 1.2rem;
            margin-top: 20px;
            margin-bottom: 15px;
        }
    </style>

    <hr style="border-color: #3a3a55;">
    <div class="connect-title">Connect With Me</div>

    <a href="mailto:email@example.com" target="_blank" class="social-link">
        <img src="https://cdn-icons-png.flaticon.com/512/732/732200.png" alt="Email">
        email@example.com
    </a>
    <a href="#" target="_blank" class="social-link">
        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn">
        LinkedIn
    </a>
    <a href="#" target="_blank" class="social-link">
        <img src="https://cdn-icons-png.flaticon.com/512/733/733553.png" alt="GitHub">
        GitHub
    </a>
    <a href="#" target="_blank" class="social-link">
        <img src="https://cdn-icons-png.flaticon.com/512/1384/1384060.png" alt="YouTube">
        The Wonder Why
    </a>

    <hr style="border-color: #3a3a55; margin-top: 25px;">
    
    <a href="#" class="download-btn">
        📄 Download Resume
    </a>
    """, unsafe_allow_html=True)


# --- 1. HOME PAGE ---
if page == "Home":
    # 1. Python reads your local image and turns it into code
    def get_image_base64(image_path):
        try:
            with open(image_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode()
        except:
            return "" # If it can't find the file, it won't crash

    # Make sure this matches your exact file name (profile.jpg or profile.png)
    img_base64 = get_image_base64("profile.jpg") 

    # 2. We inject that code into your HTML using an f-string (notice the 'f' before the quotes)
    st.markdown(f"""
    <div class="hero-container">
        <img class="hero-image" src="data:image/jpeg;base64,{img_base64}" alt="Profile Picture">
        <br>
        <div class="hero-title">HARSH GURJAR</div>
        <div class="hero-subtitle">Creator of 'The Wonder Why' | AI Engineer | Video Editor</div>
        <div class="hero-text">
            Welcome to my digital space. I bridge the gap between complex AI technology 
            and cinematic visual storytelling. Through my channel, <b>The Wonder Why</b>, I explore facts about the entire universe, 
            combining precise scriptwriting, Text-to-Speech (TTS) pipelines, and dynamic video editing to bring mysteries to life.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("🏆 Certifications & Achievements")
    cert_col1, cert_col2 = st.columns(2, gap="medium")
    with cert_col1:
        try:
            st.image("cert1.png", caption="Advanced AI & Prompt Engineering", use_container_width=True)
        except:
            st.info("Upload 'cert1.png' to your folder to display your first certificate.")
            
    with cert_col2:
        try:
            st.image("cert2.png", caption="Professional Video Editing", use_container_width=True)
        except:
            st.info("Upload 'cert2.png' to your folder to display your second certificate.")
    
    st.markdown("---")
    
    # --- TECHNICAL ARSENAL CARDS ---
    st.subheader("🛠️ Technical Arsenal")
    
    st.markdown("""
        <div class="vertical-card">
            <img class="tech-img" src="https://cdn-icons-png.flaticon.com/512/2083/2083213.png" alt="AI Icon">
            <div class="vertical-text-content">
                <div class="animated-title title-ai">AI & Engineering</div>
                <div class="tech-brief">Crafting precise LLM instructions and automated voice synthesis pipelines.</div>
                <div class="tech-text">
                    <span class="tech-text-item">• Prompt Engineering</span> &nbsp;|&nbsp; 
                    <span class="tech-text-item">• TTS Voice Workflows</span> &nbsp;|&nbsp; 
                    <span class="tech-text-item">• LLMs (OpenAI, Gemini)</span>
                </div>
            </div>
        </div>

        <div class="vertical-card">
            <img class="tech-img" src="https://cdn-icons-png.flaticon.com/512/1055/1055661.png" alt="Strategy Icon">
            <div class="vertical-text-content">
                <div class="animated-title title-strategy">Content Strategy</div>
                <div class="tech-brief">Orchestrating universe explorations, from factual research to dynamic scripts.</div>
                <div class="tech-text">
                    <span class="tech-text-item">• Universe Fact Research</span> &nbsp;|&nbsp; 
                    <span class="tech-text-item">• Scriptwriting</span> &nbsp;|&nbsp; 
                    <span class="tech-text-item">• Storyboarding</span>
                </div>
            </div>
        </div>

        <div class="vertical-card">
            <img class="tech-img" src="https://cdn-icons-png.flaticon.com/512/3112/3112521.png" alt="Video Icon">
            <div class="vertical-text-content">
                <div class="animated-title title-video">Video Production</div>
                <div class="tech-brief">Blending seamless edits, visual effects, and high-quality audio mastering.</div>
                <div class="tech-text">
                    <span class="tech-text-item">• Premiere Pro & AE</span> &nbsp;|&nbsp; 
                    <span class="tech-text-item">• DaVinci Resolve</span> &nbsp;|&nbsp; 
                    <span class="tech-text-item">• Audio Mixing</span>
                </div>
            </div>
        </div>
        
        <div class="vertical-card">
            <img class="tech-img" src="https://cdn-icons-png.flaticon.com/512/1041/1041916.png" alt="Design Icon">
            <div class="vertical-text-content">
                <div class="animated-title title-design">Designer</div>
                <div class="tech-brief">Designing vibrant thumbnails and cohesive brand assets that capture attention.</div>
                <div class="tech-text">
                    <span class="tech-text-item">• Thumbnail Creation</span> &nbsp;|&nbsp; 
                    <span class="tech-text-item">• Photoshop & Illustrator</span> &nbsp;|&nbsp; 
                    <span class="tech-text-item">• Visual Composition</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # --- GET IN TOUCH FORM ---
    st.markdown("---")
    st.subheader("📬 Get In Touch")
    st.write("Have a project in mind or want to collaborate on 'The Wonder Why'? Send me a message!")
    
    # Custom CSS for the contact form inputs
    st.markdown("""
    <style>
    input[type=text], input[type=email], textarea {
        width: 100%;
        padding: 12px;
        border: 1px solid #3a3a55;
        border-radius: 8px;
        box-sizing: border-box;
        margin-top: 6px;
        margin-bottom: 16px;
        resize: vertical;
        background-color: rgba(30, 30, 47, 0.6);
        color: white;
        font-family: 'Inter', sans-serif;
    }
    input[type=text]:focus, input[type=email]:focus, textarea:focus {
        outline: none;
        border-color: #E94057;
        box-shadow: 0 0 8px rgba(233, 64, 87, 0.4);
    }
    input[type=submit] {
        background: linear-gradient(45deg, #8A2387, #E94057, #F27121);
        color: white;
        padding: 12px 25px;
        border: none;
        border-radius: 25px;
        cursor: pointer;
        font-family: 'Inter', sans-serif;
        font-weight: bold;
        transition: all 0.3s;
    }
    input[type=submit]:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(233, 64, 87, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

    # HTML Form using FormSubmit.co
    contact_form = """
    <form action="https://formsubmit.co/YOUR_EMAIL_HERE" method="POST" style="background: linear-gradient(145deg, #1e1e2f, #2a2a40); padding: 40px; border-radius: 15px; border: 1px solid #3a3a55; box-shadow: 0 4px 10px rgba(0,0,0,0.2); max-width: 800px;">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your Message Here" required style="height: 150px;"></textarea>
        <input type="submit" value="Send Message 🚀">
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)


# --- 2. AI & PROMPT ENGINEERING PAGE ---
elif page == "AI & Prompt Engineering":
    st.markdown('<p class="hero-title" style="font-size: 2.5rem;">AI & Prompt Playground</p>', unsafe_allow_html=True)
    st.write("A deep dive into how I leverage AI tools to streamline content creation and generate high-quality outputs.")
    st.markdown("---")
    
    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.subheader("Project: Automated TTS Voiceover Pipeline")
        st.write("Integrated advanced Text-to-Speech models to generate natural, highly engaging voiceovers for every video on 'The Wonder Why', ensuring consistent, high-quality audio across all universe exploration topics.")
    with col2:
        st.subheader("Project: Structured Script Generation")
        st.write("Utilized advanced prompt engineering techniques to research, structure, and refine a highly engaging documentary-style script covering the 10 rarest animals on Earth, focusing on strict factual accuracy and audience retention.")


# --- 3. VIDEO EDITING PAGE ---
elif page == "Video Editing":
    st.markdown('<p class="hero-title" style="font-size: 2.5rem;">Video Editing Gallery</p>', unsafe_allow_html=True)
    st.write("A collection of my creative work, blending traditional editing techniques with AI-generated audio and assets.")
    st.markdown("---")
    
    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.subheader("The Wonder Why - Universe Facts")
        st.video("https://www.youtube.com/watch?v=tPEE9ZwTmy0") 
        st.write("**Role:** Lead Editor, Writer & AI Audio Director")
    with col2:
        st.subheader("Nature Mini-Doc: Rarest Animals")
        st.video("https://www.youtube.com/watch?v=34Na4j8HLjc") 
        st.write("**Role:** Creator & Editor")


# --- 4. CHAT WITH AI CLONE PAGE ---
elif page == "Chat with My AI Clone":
    st.markdown('<p class="hero-title" style="font-size: 2.5rem;">Chat with My AI Clone</p>', unsafe_allow_html=True)
    st.write("Ask my digital twin about my channel, my editing process, or my tech stack!")
    st.markdown("---")

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Stop wondering and start knowing. Welcome to The Wonder Why. Let's dive into the facts about my portfolio! What would you like to know?"}
        ]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Bulletproof input check
    prompt = st.chat_input("Ask me about the universe, TTS, or video editing...")
    
    if prompt:
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        if "bye" in prompt.lower() or "goodbye" in prompt.lower() or "exit" in prompt.lower():
            response = "The universe hides the truth, but we bring the facts—by becoming a part of The Wonder Why you never miss any mysteries, and I'll see you in the next one."
        else:
            response = f"That's a great question about '{prompt}'. I'm currently a prototype clone, but I'm built to share facts about the entire universe and my creator's video editing process!"
        
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})