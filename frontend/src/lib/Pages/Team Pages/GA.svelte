<script lang="ts">
    import NavBar from "../../Components/NavBar.svelte";
    import HeadShot from "../../Components/HeadShot.svelte";
    import KarimElguindy from "../../../assets/AC/GA-A/Karim Elguindy- GA A chair.jpg"
    import LaylaMourad from "../../../assets/AC/GA-A/Layla Mourad - GA A cochair.jpg"
    import MalakShawky from "../../../assets/AC/GA-B/Malak Shawky-GAB cochair.jpg"
    import CynthiaEzzi from "../../../assets/AC/GA-B/Cynthia Ezzi - GAB  co chair.jpg"
    import PlaceHolder from "../../../assets/PlaceHolder.jpeg"
</script>
  

<body class="bg-cover bg-no-repeat bg-center" >
    <NavBar />

    <div class="p-10">
        <h1 class="text-center text-4xl font-bold mb-2">Chairs of the General Assembly</h1>
        <hr class="mb-4">
        <h1 class="text-left text-3xl font-bold mb-2">GA-A:</h1>
        <hr class="mb-4">
        <div class="grid grid-flow-row grid-rows-3 space-y-2 mb-4">
            <section class="grid row-span-2 grid-cols-1 md:grid-cols-2 gap-4  rounded shadow-md row-span-1">
                <div class="relative flex p-5">
                    <img src={KarimElguindy} alt="Person" class="object-cover rounded-lg w-full"/>
                </div>
                <div class="flex flex-col justify-between">
                    <div class="">
                        <div class="font-bold text-2xl text-gray-800 mb-3 mt-7">
                            <header>Karim Elguindy - Chair of the General Assembly A</header>
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
                <HeadShot name="Layla Mourad" title="Co-Chair" image={LaylaMourad} quote="With determination anything is achievable"/>
                <HeadShot name="Youssef Sheriff" title="Co-Chair" image={PlaceHolder} quote="Sometimes all you need is a little imagination"/>
            </div>
        </div>

        <h1 class="text-left text-3xl font-bold mb-2">HRC-B:</h1>
        <hr class="mb-4">
        <div class="grid grid-flow-row grid-rows-3 space-y-2 ">
            <section class="grid row-span-2 grid-cols-1 md:grid-cols-2 gap-4  rounded shadow-md row-span-1">
                <div class="relative flex p-5">
                    <img src={PlaceHolder} alt="Person" class="object-cover rounded-lg w-full"/>
                </div>
                <div class="flex flex-col justify-between">
                    <div class="">
                        <div class="font-bold text-2xl text-gray-800 mb-3 mt-7">
                            <header>Omar Fazary - Chair of the General Assembly B</header>
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
                <HeadShot name="Malak Shawky" title="Co-Chair" image={MalakShawky} quote="With determination anything is achievable"/>
                <HeadShot name="Cynthia Ezzi" title="Co-Chair" image={CynthiaEzzi} quote="Sometimes all you need is a little imagination"/>
            </div>
        </div>
    </div>
</body>