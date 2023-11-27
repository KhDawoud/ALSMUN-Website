<script lang="ts">
    import NavBar from "../../Components/NavBar.svelte";
    import Banner from "../../Components/Banner.svelte";
    import JazminBlaj from "../../../assets/Secretariat/Jazmin Blaj.jpg"
    import MariamElRamly from "../../../assets/Secretariat/Mariam Elramly.jpg"
    import IbrahimZineldin from "../../../assets/Secretariat/Ibrahim Zineldin - DSG.jpg"
    import AdhamFayed from "../../../assets/Secretariat/Adham Fayed - USG.jpg"
  </script>
  
  
  <NavBar />
  
  <main class="grid grid-flow-row grid-rows-4 space-y-5 m-5">
    <section class="grid grid-cols-1 md:grid-cols-2 gap-4 row-span-1 rounded shadow-md">
        <div class="relative flex p-5">
            <img src={JazminBlaj} alt="Person" class="object-cover rounded-lg w-full"/>
        </div>
        <div class="flex flex-col justify-between">
            <div class="">
                <div class="font-bold text-2xl text-gray-800 mb-3 mt-7">
                    <header>Jazmin Blaj - Secretary General</header>
                    <hr>
                </div>
                <div>
                    <article class=" text-sm md:text-base">
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate 
                    </article>
                </div>
            </div> 
        </div>
    </section>
    <section class="grid grid-cols-1 md:grid-cols-2 gap-4 row-span-1 rounded shadow-md">
        <div class="relative flex p-5">
            <img src={IbrahimZineldin} alt="Person" class="object-cover rounded-lg w-full"/>
        </div>
        <div class="flex flex-col justify-between">
            <div class="">
                <div class="font-bold text-2xl text-gray-800 mb-3 mt-7">
                    <header>Ibrahim Zineldin - Deputy Secretary General</header>
                    <hr>
                </div>
                <div>
                    <article class=" text-sm md:text-base">
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate 
                    </article>
                </div>
            </div> 
        </div>
    </section>
    <section class="grid grid-cols-1 md:grid-cols-2 gap-4 row-span-1 rounded shadow-md">
        <div class="relative flex p-5">
            <img src={AdhamFayed} alt="Person" class="object-cover rounded-lg w-full"/>
        </div>
        <div class="flex flex-col justify-between">
            <div class="">
                <div class="font-bold text-2xl text-gray-800 mb-3 mt-7">
                    <header>Adham Fayed - Under Secretary General</header>
                    <hr>
                </div>
                <div>
                    <article class=" text-sm md:text-base">
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate 
                    </article>
                </div>
            </div> 
        </div>
    </section>
    <section class="grid grid-cols-1 md:grid-cols-2 gap-4 row-span-1 rounded shadow-md">
        <div class="relative flex p-5">
            <img src={MariamElRamly} alt="Person" class="object-cover rounded-lg w-full"/>
        </div>
        <div class="flex flex-col justify-between">
            <div class="">
                <div class="font-bold text-2xl text-gray-800 mb-3 mt-7">
                    <header>Mariam ElRamly - Assistant Secretary General</header>
                    <hr>
                </div>
                <div>
                    <article class=" text-sm md:text-base">
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate 
                    </article>
                </div>
            </div> 
        </div>
    </section>
  </main>