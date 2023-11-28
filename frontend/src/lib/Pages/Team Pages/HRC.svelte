<script lang="ts">
    import NavBar from "../../Components/NavBar.svelte";
    import HeadShot from "../../Components/HeadShot.svelte";
    import SalmaSaber from "../../../assets/AC/HRC-A/Salma Saber - HRC A chair.jpg"
    import MayaDaader from "../../../assets/AC/HRC-A/Maya Daader - HRC A co chair.jpg"
    import ZiadMedhat from "../../../assets/AC/HRC-A/Ziad Medhat - HRC A co chair.jpg"
    import OmarElHefnawy from "../../../assets/AC/HRC-B/Omar Elhefnawy - HRC B chair.jpg"
    import NourSalah from "../../../assets/AC/HRC-B/Nour Salah - HRC B co chair.jpg"
    import HabibaKholeif from "../../../assets/AC/HRC-B/Habiba Kholeif - HRC B co chair.jpg"
</script>
  

<body class="bg-cover bg-no-repeat bg-center" >
    <NavBar />

    <div class="p-10">
        <h1 class="text-center text-4xl font-bold mb-2">Chairs of the Human Rights Council</h1>
        <hr class="mb-4">
        <h1 class="text-left text-3xl font-bold mb-2">HRC-A:</h1>
        <hr class="mb-4">
        <div class="grid grid-flow-row grid-rows-3 space-y-2 mb-4">
            <section class="grid row-span-2 grid-cols-1 md:grid-cols-2 gap-4  rounded shadow-md row-span-1">
                <div class="relative flex p-5">
                    <img src={SalmaSaber} alt="Person" class="object-cover rounded-lg w-full"/>
                </div>
                <div class="flex flex-col justify-between">
                    <div class="">
                        <div class="font-bold text-2xl text-gray-800 mb-3 mt-7">
                            <header>Salma Saber - Chair of the Human Rights Council A</header>
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
                <HeadShot name="Maya Daader" title="Co-Chair" image={MayaDaader} quote="With determination anything is achievable"/>
                <HeadShot name="Ziad Medhat" title="Co-Chair" image={ZiadMedhat} quote="Sometimes all you need is a little imagination"/>
            </div>
        </div>

        <h1 class="text-left text-3xl font-bold mb-2">HRC-B:</h1>
        <hr class="mb-4">
        <div class="grid grid-flow-row grid-rows-3 space-y-2 ">
            <section class="grid row-span-2 grid-cols-1 md:grid-cols-2 gap-4  rounded shadow-md row-span-1">
                <div class="relative flex p-5">
                    <img src={OmarElHefnawy} alt="Person" class="object-cover rounded-lg w-full"/>
                </div>
                <div class="flex flex-col justify-between">
                    <div class="">
                        <div class="font-bold text-2xl text-gray-800 mb-3 mt-7">
                            <header>Omar El Hefnawy - Chair of the Human Rights Council B</header>
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
                <HeadShot name="Nour Salah" title="Co-Chair" image={NourSalah} quote="With determination anything is achievable"/>
                <HeadShot name="Habiba Kholeif" title="Co-Chair" image={HabibaKholeif} quote="Sometimes all you need is a little imagination"/>
            </div>
        </div>
    </div>
</body>