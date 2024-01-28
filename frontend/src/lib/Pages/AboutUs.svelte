<script>
    import CountDown from "../Components/CountDown.svelte";
    import NavBar from "../Components/NavBar.svelte";
    import SchoolBackground from '../../assets/SchoolBackground.jpeg';
    import Tiktok from "../../assets/Icons/Tiktok.ico";
    import Instagram from "../../assets/Icons/Instagram.ico";
</script>

<NavBar/>

<div class ="flex items-center justify-center bg-cover bg-no-repeat bg-center w-full h-[30rem] px-10 mb-10" style="background-image: url('{SchoolBackground}');">
    <div class ="text-white text-8xl font-extrabold text-center">About Us</div>
</div>

<div class="grid grid-cols-3 px-3">
    <div class="col-span-2 p-3">
        <div class="mb-12">
            <h1 class="text-3xl font-bold"> About ALSMUN2</h1>
            <hr class="my-2">
            <p class="mt-5">ALSMUN is proud to be hosting its first open conference to students in Egypt this year. We have participated in many conferences around the world as delegates and chairs in the past and are ecstatic to bring Alssonian pride and spirit into the MUN community formally. ALSMUN will be a conference for delegates to grow intellectually and expand their understanding and comfort discussing international politics, reinforcing their social skills and public speaking.
            </p>
            
        </div>
        <div class="mb-12">
            <h1 class="text-3xl font-bold mb-7">A Letter From The Secretary General</h1>
            <div class="mx-auto w-40% h-80% border-2 border-yellow-500 rounded-lg ">
                <p class="text-base/6 mx-20 my-10 hover:mx-10 hover:my-5 ease-in-out duration-200">“But there’s always a first time for everything” is what they say. <br><br>
                They speak of trial and error, the struggle to wrap your head around it all and most importantly - the pride of having achieved something. 
                That is what we want ALSMUNII to teach. <br><br>
                
                My name is Jazmin Blaj and I am extremely honoured to be able to deliver ALSMUNII to you all as the Secretary General. Alongside our team, we have meticulously designed and created this conference to honour the belief that less is more and showcase the importance of quality over quantity. 
                Let ALSMUNII be an opportunity for you to grow and learn, and make the most of it. 
                Whether you're afraid to speak up, fight back or stand for what you think is right, take the plunge. <br><br>
                
                There’s a first time for everything… right?
                </p>
            </div>
            
        </div>  
    </div>
    <div class="border rounded-3xl overflow-hidden mb-10">
        <div class="p-5 border-2" style="border-image: linear-gradient(to right, #FAD628, #FAA428); border-image-slice: 1;">
            <h1 class="text-3xl font-bold text-center">Sections</h1>
            <hr class="w-full my-4 border-none bg-gradient-to-r from-yellow-500 to-yellow-600 h-1">
            <ol>
                <li class="flex items-center w-full h-12 hover:bg-gray-100 px-3 rounded-xl hover:border-b-2 transition-all ease-in duration-100" style="border-image: linear-gradient(to right, #3498db, #9b59b6); border-image-slice: 1;">About ALSMUN2</li>
                <li class="flex items-center w-full h-12 hover:bg-gray-100 px-3 rounded-xl hover:border-b-2 transition-all ease-in duration-100" style="border-image: linear-gradient(to right, #3498db, #9b59b6); border-image-slice: 1;">Letter From Secretariat</li>
                <li class="flex items-center w-full h-12 hover:bg-gray-100 px-3 rounded-xl hover:border-b-2 transition-all ease-in duration-100" style="border-image: linear-gradient(to right, #3498db, #9b59b6); border-image-slice: 1;">A Look Into ALSMUN1</li>
            </ol>
        </div>
    </div>
</div>

<footer class="bg-gray-800 text-white p-6 text-center">

    <p class="text-xl font-bold mb-4">ALSMUN II</p>

    <div class="flex justify-center space-x-4">
        <a href="https://www.instagram.com/elalssonmun/" class="text-white hover:text-gray-500 mx-2">
            <img src={Instagram} alt="Instagram" width=40 height=40/>
        </a>
        <a href="/" class="text-white hover:text-gray-500 mx-2">
            <img src={Tiktok} alt="Tiktok" width=40 height=40/>
        </a>
        <a href="/" class="text-white hover:text-gray-500 mx-2">
            <i class="fab fa-instagram"></i>
        </a>
    </div>
</footer>
