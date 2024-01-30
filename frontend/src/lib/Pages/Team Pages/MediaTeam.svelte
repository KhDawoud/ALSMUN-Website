<script lang="ts">
    import NavBar from "../../Components/NavBar.svelte";
    import HeadShot from "../../Components/HeadShot.svelte";
    import SelimElMeadawy from "../../../assets/OC/Media/Selim Meadawy - Media and Photography.jpg"
    import MagdiBittar from "../../../assets/OC/Media/MagdiBittar.jpg";
    import PlaceHolder from "../../../assets/Icons/Default_pfp.svg"
    import GroupSection from "../../Components/GroupSection.svelte";
</script>
  

    <NavBar />
    <header class="px-10">
        <h1 class=" text-6xl font-bold text-center mt-10"> Our Media Team </h1>
        <hr class="mb-2 mt-4">  
    </header>
    <main class="grid grid-cols-4 m-5 space-x-4 space-y-4 p-5">
        <div class="mt-4 ms-4">
            <HeadShot name="Hussein Namek" title="Interviewer 1" image={PlaceHolder} quote=" "/>
        </div>  
        <HeadShot name="Seif El Aref" title="Photographer 1" image={PlaceHolder} quote=""/>
        <HeadShot name="Nazly Helmy" title="Interviewer 2" image={PlaceHolder} quote=" "/>
        <HeadShot name="Sherine Wally" title="Photographer 2" image={PlaceHolder} quote=" "/>
        <HeadShot name="Jana Samhan" title="Interviewer 3" image={PlaceHolder} quote=" "/>
        <HeadShot name="Talia Seoudy" title="Photographer 3" image={PlaceHolder} quote=" "/>
        <HeadShot name="Farida Shawky" title="Interviewer 4" image={PlaceHolder} quote=" "/>
        <HeadShot name="Jana Shahin" title="Photographer 4" image={PlaceHolder} quote=" "/>
        <HeadShot name="Aline Wahba" title="Interviewer 5" image={PlaceHolder} quote=" "/>
        <HeadShot name="Judi Nassar" title="Photographer 5" image={PlaceHolder} quote=" "/>
        <HeadShot name="Haya Abou El Nasr" title="Interviewer 6" image={PlaceHolder} quote=" "/>
        <HeadShot name="Farah Ibrahim" title="Photographer 6" image={PlaceHolder} quote=" "/>
        <HeadShot name="Farida Khalil" title="Interviewer 7" image={PlaceHolder} quote=" "/>
        <HeadShot name="Habiba Khalil" title="Photographer 7" image={PlaceHolder} quote=" "/>
        <HeadShot name="Magdi El Bittar" title="Interviewer 8" image={MagdiBittar} quote=" "/>
        <HeadShot name="Selim El Meadawy" title="Photographer 8" image={SelimElMeadawy} quote=" "/>
        
        
        
        
        

        
        
        
    </main>

