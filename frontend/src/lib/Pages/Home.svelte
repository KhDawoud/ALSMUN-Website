<script>
    import NavBar from "../Components/NavBar.svelte";
    import SchoolBackground from '../../assets/Background/Background2.jpg';
    import Instagram from "../../assets/Icons/Instagram.ico";
    import Image1 from "../../assets/Home/1.jpg"
    import JBSignature from "../../assets/Signatures/JB.png";
    import Carousel from "../Components/Carousel.svelte";
    import Schedule1 from "../../assets/Home/Schedule1.jpg";
    import Schedule2 from "../../assets/Home/Schedule2.jpg";
    import Schedule3 from "../../assets/Home/Schedule3.jpg";
    import RahmaZein from "../../assets/Home/RahmaZein.jpg"
    let images = [Schedule1, Schedule2, Schedule3]
</script>


<NavBar/>

<div class ="flex items-center justify-center bg-cover bg-no-repeat bg-center w-full h-96 px-10" style="background-image: url('{SchoolBackground}');">
    <div class ="sticky text-white text-7xl md:text-8xl font-extrabold text-center">ALSMUNII</div>
</div>

<div class="px-8 mt-10">
    <section class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-3">
            <div class="pt-3 pb-5 md:py-6 md:px-7 px-4 flex flex-col justify-between">
                <div class="mb-4 md:mb-0">
                    <div class="text-center font-bold text-4xl text-gray-800 mb-3">
                        <header>Welcome to ALSMUNII</header>
                        <hr class="my-3 border-none bg-gradient-to-r from-blue-500 to-purple-500 h-1">
                    </div>
                    <div>
                        <article class="md:mt-10 md:text-lg text-sm ">
                            ALSMUN is proud to be hosting its first open conference to students in Egypt this year. We have participated in many conferences around the world as delegates and chairs in the past and are ecstatic to bring Alssonian pride and spirit into the MUN community formally. ALSMUN will be a conference for delegates to grow intellectually and expand their understanding and comfort discussing international politics, reinforcing their social skills and public speaking.
            
                        </article>
                    </div>
                </div> 
            </div>
            <div class="relative flex">
                <img src={Image1} alt="First ALSMUN Confrenece" class="object-cover w-full"/>
            </div>
        </section>
    <hr>
</div>


<h1 class="px-8 text-2xl md:text-4xl font-semibold opacity-20 my-10">First Things First...</h1>

<div class="px-10">
    <header class="text-4xl text-center font-bold"> Your Schedule </header> 
    <hr class="my-5">
    <Carousel perPage={1} duration={600}>
        {#each images as image}
          <div class="flex items-center justify-center h-fit">
            <img src={image} alt="Schedule"/>
          </div>
        {/each}
        <span slot="left-control" class= "text-9xl text-slate-700">&laquo;</span>
        <span slot="right-control" class ="text-9xl text-slate-700">&raquo;</span>
    </Carousel>
    <hr class="my-5">
</div>


<h1 class="px-8 text-2xl md:text-4xl font-semibold opacity-30 my-10"> And Now A Quick...</h1>

<div class="mx-10 md:border md:px-5 md:pt-12 md:pb-8 rounded-2xl">
    <header class="text-center text-4xl md:text-6xl font-bold"> Letter From The Secretariat </header>
    <hr class="my-5 border-none bg-gradient-to-r from-blue-500 to-purple-500 h-1">
    <section class="mt-10 mb-10 text-base md:text-lg px-7 italic">
        “But there’s always a first time for everything” is what they say. <br><br>
                They speak of trial and error, the struggle to wrap your head around it all and most importantly - the pride of having achieved something. 
                That is what we want ALSMUNII to teach. <br><br>
                
                My name is Jazmin Blaj and I am extremely honoured to be able to deliver ALSMUNII to you all as the Secretary General. Alongside our team, we have meticulously designed and created this conference to honour the belief that less is more and showcase the importance of quality over quantity. 
                Let ALSMUNII be an opportunity for you to grow and learn, and make the most of it. 
                Whether you're afraid to speak up, fight back or stand for what you think is right, take the plunge. <br><br>
                
                There’s a first time for everything… right?
        <div class="flex flex-row mt-6">
            <img src={JBSignature} alt="Jazmin Blaj Signature" class="w-[40px] md:w-[80px]"/>
        </div>
    </section>
</div>


<h1 class="px-8 text-2xl md:text-4xl font-semibold opacity-30 my-10"> And Finally A Quick Word About...</h1>

<div class="px-8 mt-10 mb-8">
    <section class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-3">
            <div class="pt-3 pb-5 md:py-6 md:px-7 px-4 flex flex-col justify-between">
                <div class="mb-4 md:mb-0">
                    <div class="text-center font-bold text-4xl text-gray-800 mb-3">
                        <header>Our Guest Speaker</header>
                        <hr class="my-3 border-none bg-gradient-to-r from-blue-500 to-purple-500 h-1">
                    </div>
                    <div>
                        <article class="md:mt-6 md:text-base text-sm ">
                            Rahma Zein is an Egyptian podcaster and Editor in Chief of Scoop Empire. She is most recently recognized for fearlessly raising her voice to confront CNN's English reporter, Clarissa Ward. In the now-viral footage, Zein's words are directed towards Ward, questioning her empathy and humanity during the ongoing events. Zein had spent the previous night sleeping in a tent at the Rafah crossing, hearing airstrikes land on Gaza's inhabitants on the other side of the border. Hundreds of volunteers, including her, were waiting for the border to open in order to send aid into Gaza. Zein received an invitation to appear on Prominent British broadcaster Piers Morgan's talk show, "Uncensored." who is well-known for doing provocative interviews. Rahma contested the problematic worldwide rhetoric surrounding Arabs in favor of equality in Palestine during the 16-minute conversation, as well as the purposefully sensationalist perspective Morgan was attempting to put her in. Since its initial release, the interview has received over 3.2 million views on YouTube, mainly positive comments for Rahma's perspectives. Rahma Zein's statements speak to a great number of young people who stand up for justice and the truth in the face of injustice. Her powerful rhetoric demonstrates her commitment to humanitarian causes and a sense of responsibility. More powerful and encouraging voices like Rahma Zein are needed in the world. She is a brilliant example of how young people can take on social duty and fight for justice and human rights.
                        </article>
                    </div>
                </div> 
            </div>
            <div class="relative flex">
                <img src={RahmaZein} alt="First ALSMUN Confrenece" class="object-cover w-full"/>
            </div>
        </section>
    <hr>
</div>



<footer class="bg-gray-800 text-white p-6 text-center">

    <p class="text-xl font-bold mb-4">ALSMUN II</p>

    <div class="flex justify-center space-x-4">
        <a href="https://www.instagram.com/elalssonmun/" class="text-white hover:text-gray-500 mx-2">
            <img src={Instagram} alt="Instagram" width=40 height=40/>
        </a>
    </div>
</footer>
