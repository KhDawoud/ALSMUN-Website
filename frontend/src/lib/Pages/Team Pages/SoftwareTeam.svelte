<script lang="ts">
  import AliElGuindy from '../../../assets/OC/SoftwareTeam/Ali Guindy.jpg';
  import NavBar from "../../Components/NavBar.svelte";
  import KhaledDawoud from '../../../assets/OC/SoftwareTeam/Khaled Dawoud.jpg';
  import HeadShot from "../../Components/HeadShot.svelte";
  import MuhammedElKhedr from '../../../assets/OC/SoftwareTeam/Muhammed elkhedr.jpg';
  import KarimElMetainy from '../../../assets/OC/SoftwareTeam/Karim El Metainy.jpg';
  import Background from "../../../assets/Alt2.svg";


</script>

<body class="bg-cover bg-no-repeat bg-center" >
    <NavBar />

    <div class="p-10">
        <h1 class="text-center text-4xl font-bold mb-2"> Our Software Developers </h1>
        <hr class="mb-4">
        <div class="grid grid-flow-row grid-rows-2 space-y-2">
            <section class="grid grid-cols-1 md:grid-cols-2 gap-4  rounded shadow-md">
                <div class="relative flex p-5">
                    <img src={KarimElMetainy} alt="Person" class="object-cover rounded-lg w-full"/>
                </div>
                <div class="flex flex-col justify-between">
                    <div class="">
                        <div class="font-bold text-2xl text-gray-800 mb-3 mt-7">
                            <header>Head Of Software Development</header>
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
            <div class="grid grid-cols-3 grid-flow-col space-x-2">
                <HeadShot name="Khaled Dawoud" title="Lead Developer" image={KhaledDawoud} quote="With determination anything is achievable"/>
                <HeadShot name="Ali El Guindy" title="UI Designer" image={AliElGuindy} quote="Sometimes all you need is a little imaginations"/>
                <HeadShot name="Muhammed El Khedr" title="Frontend Developer" image={MuhammedElKhedr} quote="Difficult roads often lead to beautiful destinations"/>
            </div>
        </div>
    </div>
</body>