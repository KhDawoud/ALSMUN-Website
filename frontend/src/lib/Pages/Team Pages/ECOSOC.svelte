<script lang="ts">
    import NavBar from "../../Components/NavBar.svelte";
    import HeadShot from "../../Components/HeadShot.svelte";
    import OmarEzzi from "../../../assets/AC/ECOSOC-A/Omar Elezzi- ECOSOC A chair.jpg"
    import SalmaShayal from "../../../assets/AC/ECOSOC-A/Salma Shayal - ECOSOC A cochair.jpg"
    import AdamYoussef from "../../../assets/AC/ECOSOC-A/Adam Youssef - ECOSOC A co chair.jpg"
    import AlaaHashem from "../../../assets/AC/ECOSOC-B/Alaa Hashem - Chair of ECOSOC B.jpg"
    import HabibaRaslan from "../../../assets/AC/ECOSOC-B/Habiba Raslan - ECOSOC B co chair.jpg"
    import MahmoudHelmy from "../../../assets/AC/ECOSOC-B/Mahmoud Helmy- ECOSOC B co chair.jpg"
</script>
  

<body class="bg-cover bg-no-repeat bg-center" >
    <NavBar />

    <div class="p-10">
        <h1 class="text-center text-4xl font-bold mb-2">Chairs of the Econonomic and Social Council</h1>
        <hr class="mb-4">
        <h1 class="text-left text-3xl font-bold mb-2">ECOSOC-A:</h1>
        <hr class="mb-4">
        <div class="grid grid-flow-row grid-rows-3 space-y-2 mb-4">
            <section class="grid row-span-2 grid-cols-1 md:grid-cols-2 gap-4  rounded shadow-md row-span-1">
                <div class="relative flex p-5">
                    <img src={OmarEzzi} alt="Person" class="object-cover rounded-lg w-full"/>
                </div>
                <div class="flex flex-col justify-between">
                    <div class="">
                        <div class="font-bold text-2xl text-gray-800 mb-3 mt-7">
                            <header>Omar Ezzi - Chair of the Econonomic and Social Council A</header>
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
            <div class="grid grid_cols_2 grid-flow-col space-x-2 h-[30rem]">
                <HeadShot name="Salma Shayal" title="Co-Chair" image={SalmaShayal} quote="With determination anything is achievable"/>
                <HeadShot name="Adam Youssef" title="Co-Chair" image={AdamYoussef} quote="Sometimes all you need is a little imagination"/>
            </div>
        </div>

        <h1 class="text-left text-3xl font-bold mb-2">ECOSOC-B:</h1>
        <hr class="mb-4">
        <div class="grid grid-flow-row grid-rows-3 space-y-2 ">
            <section class="grid row-span-2 grid-cols-1 md:grid-cols-2 gap-4  rounded shadow-md row-span-1">
                <div class="relative flex p-5">
                    <img src={AlaaHashem} alt="Person" class="object-cover rounded-lg w-full"/>
                </div>
                <div class="flex flex-col justify-between">
                    <div class="">
                        <div class="font-bold text-2xl text-gray-800 mb-3 mt-7">
                            <header>Alaa Hashem - Chair of the Economic and Social Council B</header>
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
            <div class="grid grid_cols_2 grid-flow-col space-x-2 h-[30rem]">
                <HeadShot name="Habiba Raslan" title="Co-Chair" image={HabibaRaslan} quote="With determination anything is achievable"/>
                <HeadShot name="Mahmoud Helmy" title="Co-Chair" image={MahmoudHelmy} quote="Sometimes all you need is a little imagination"/>
            </div>
        </div>
    </div>
</body>