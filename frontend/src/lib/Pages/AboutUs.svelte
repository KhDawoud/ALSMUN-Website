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
    <div class="col-span-2">
        <h1> Rest Of Content</h1>
    </div>
    <div class="border rounded-3xl overflow-hidden mb-10">
        <div class="p-5 border-2" style="border-image: linear-gradient(to right, #3498db, #9b59b6); border-image-slice: 1;">
            <h1 class="text-3xl font-bold text-center">Sections</h1>
            <hr class="w-full my-4 border-none bg-gradient-to-r from-blue-500 to-purple-500 h-1">
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
        <a href="/" class="text-white hover:text-gray-500 mx-2">
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
