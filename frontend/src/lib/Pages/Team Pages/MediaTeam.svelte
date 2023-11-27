<script lang="ts">
    import NavBar from "../../Components/NavBar.svelte";
    import HeadShot from "../../Components/HeadShot.svelte";
    import SelimElMeadawy from "../../../assets/OC/Media/Selim Meadawy - Media and Photography.jpg"
    import PlaceHolder from "../../../assets/PlaceHolder.jpeg"
</script>
  

<body class="bg-cover bg-no-repeat bg-center" >
    <NavBar />

    <div class="p-10">
        <h1 class="text-center text-4xl font-bold mb-2"> The Media Team</h1>
        <hr class="mb-4">
        <div class="grid grid-flow-row grid-rows-3 space-y-2 ">
            <section class="grid grid-cols-1 md:grid-cols-2 gap-4  rounded shadow-md row-span-1">
                <div class="relative flex p-5">
                    <img src={SelimElMeadawy} alt="Person" class="object-cover rounded-lg w-full"/>
                </div>
                <div class="flex flex-col justify-between">
                    <div class="">
                        <div class="font-bold text-2xl text-gray-800 mb-3 mt-7">
                            <header>Selim ElMeadawy</header>
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
            <section class="grid grid-cols-1 md:grid-cols-2 gap-4  rounded shadow-md row-span-1">
                <div class="relative flex p-5">
                    <img src={PlaceHolder} alt="Person" class="object-cover rounded-lg w-full"/>
                </div>
                <div class="flex flex-col justify-between">
                    <div class="">
                        <div class="font-bold text-2xl text-gray-800 mb-3 mt-7">
                            <header>Hussein Namek</header>
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
            <section class="grid grid-cols-1 md:grid-cols-2 gap-4  rounded shadow-md row-span-1">
                <div class="relative flex p-5">
                    <img src={PlaceHolder} alt="Person" class="object-cover rounded-lg w-full"/>
                </div>
                <div class="flex flex-col justify-between">
                    <div class="">
                        <div class="font-bold text-2xl text-gray-800 mb-3 mt-7">
                            <header>Magdi El Bittar</header>
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
        </div>
    </div>
</body>