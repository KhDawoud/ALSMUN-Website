<script lang="ts">
    import NavBar from "../../Components/NavBar.svelte";
    import HeadShot from "../../Components/HeadShot.svelte";
    import SelimElMeadawy from "../../../assets/OC/Media/SelimMeadawy.jpg";
    import MagdiBittar from "../../../assets/OC/Media/MagdiBittar.jpg";
    import HusseinNamek from "../../../assets/Oc/Media/HusseinNamek.jpg";
    import JudiNassar from "../../../assets/Oc/Media/JudiNassar.jpg";
    import JanaShahin from "../../../assets/Oc/Media/JanaShahin.jpg";
    import HabibaKhalil from "../../../assets/Oc/Media/HabibaKhalil.jpg";
    import AlineWahba from "../../../assets/Oc/Media/AlineWahba.jpg";
    import SherineWally from "../../../assets/Oc/Media/SherineWally.jpg";
    import TaliaSeoudi from "../../../assets/Oc/Media/TaliaSeoudi.jpg";
    import FarahIbrahim from "../../../assets/OC/Media/FarahIbrahim.jpg"
    import PlaceHolder from "../../../assets/Icons/Default_pfp.svg";
</script>
  

    <NavBar />
    <header class="px-10">
        <h1 class=" text-6xl font-bold text-center mt-10"> Our Media Team </h1>
        <hr class="mb-2 mt-4">  
    </header>
    <main class="grid md:grid-cols-3 mx-8 md:mx-12 md:space-x-4 md:space-y-0 space-y-4 px-5">
        <HeadShot name="Jana Samhan" title="Interviewer 1" image={PlaceHolder} quote = "Welcome to ALSMUNII! We can't wait to see you!"/>
        <HeadShot name="Talia Seoudy" title="Photographer 1" image={TaliaSeoudi} quote = "Welcome to ALSMUNII! We can't wait to see you!"/>
        <HeadShot name = "Souhaila Akef" title="Content Creator" image={PlaceHolder} quote="Welcome to ALSMUNII! We can't wait to see you!"/>
    </main>
    <main class="grid grid-flow-row md:grid-cols-4 mx-5 space-x-4 space-y-4 px-5">
        <div class="mt-4 ms-4">
            <HeadShot name="Hussein Namek" title="Interviewer 2" image={HusseinNamek} quote = "Welcome to ALSMUNII! We can't wait to see you!"/>
        </div>  
        <HeadShot name="Seif El Aref" title="Photographer 2" image={PlaceHolder} quote = "Welcome to ALSMUNII! We can't wait to see you!"/>
        <HeadShot name="Nazly Helmy" title="Interviewer 3" image={PlaceHolder} quote = "Welcome to ALSMUNII! We can't wait to see you!"/>
        <HeadShot name="Sherine Wally" title="Photographer 3" image={SherineWally} quote = "Welcome to ALSMUNII! We can't wait to see you!"/>
        <HeadShot name="Farida Shawky" title="Interviewer 4" image={PlaceHolder} quote = "Welcome to ALSMUNII! We can't wait to see you!"/>
        <HeadShot name="Jana Shahin" title="Photographer 4" image={JanaShahin} quote = "Welcome to ALSMUNII! We can't wait to see you!"/>
        <HeadShot name="Aline Wahba" title="Interviewer 5" image={AlineWahba} quote = "Welcome to ALSMUNII! We can't wait to see you!"/>
        <HeadShot name="Judi Nassar" title="Photographer 5" image={JudiNassar} quote = "Welcome to ALSMUNII! We can't wait to see you!"/>
        <HeadShot name="Haya Abou El Nasr" title="Interviewer 6" image={PlaceHolder} quote = "Welcome to ALSMUNII! We can't wait to see you!"/>
        <HeadShot name="Farah Ibrahim" title="Photographer 6" image={FarahIbrahim} quote = "Welcome to ALSMUNII! We can't wait to see you!"/>
        <HeadShot name="Farida Khalil" title="Interviewer 7" image={PlaceHolder} quote = "Welcome to ALSMUNII! We can't wait to see you!"/>
        <HeadShot name="Habiba Khalil" title="Photographer 7" image={HabibaKhalil} quote = "Welcome to ALSMUNII! We can't wait to see you!"/>
    </main>
    <div class="grid md:grid-cols-2 md:w-3/5 md:mx-auto md:space-x-4 md:space-y-0 space-y-4 mx-12 mt-4">
        <HeadShot name="Magdi El Bittar" title="Interviewer 8" image={MagdiBittar} quote = "Welcome to ALSMUNII! We can't wait to see you!"/>
        <HeadShot name="Selim El Meadawy" title="Photographer 8" image={SelimElMeadawy} quote = "Welcome to ALSMUNII! We can't wait to see you!"/>

    </div>
        

