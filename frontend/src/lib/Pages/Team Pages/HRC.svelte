<script lang="ts">
    import NavBar from "../../Components/NavBar.svelte";
    import GroupSection from "../../Components/GroupSection.svelte";
    import HeadShot from "../../Components/HeadShot.svelte";
    import SalmaSaber from "../../../assets/AC/HRC-A/SalmaSaber.jpg"
    import MayaDaader from "../../../assets/AC/HRC-A/MayaDaader.jpg"
    import ZiadMedhat from "../../../assets/AC/HRC-A/ZiadMedhat.jpg"
    import OmarElHefnawy from "../../../assets/AC/HRC-B/OmarElhefnawy.jpg"
    import NourSalah from "../../../assets/AC/HRC-B/NourSalah.jpg"
    import HabibaKholeif from "../../../assets/AC/HRC-B/HabibaKholeif.jpg"
</script>
  

<NavBar />
<header class="px-10">
    <h1 class=" text-4xl font-bold text-center mt-10"> Human Rights Council A </h1>
    <hr class="mb-2 mt-4">  
</header>
<section class="p-10 space-y-6">
    <GroupSection link={null} noReadMe={true} header="Salma Saber - Chair of HRC A" text={"Hi everyone! My name is Salma Saber and I'm the chair for HRC A. Why HRC? Bringing awareness to global injustices worldwide is a step in the right direction, a step that I believe should be taken more often. As it has been made clear to everyone recently, we as the human race have been lacking. As for my effort in this matter, I am a political science major hoping to benefit this world in any way I can. I can't wait to see you all soon and hopefully inspire this sense in you too, if it's not already there."} image={SalmaSaber} />
    <section class="space-x-0 space-y-2 md:grid md:grid-flow-col md:grid-cols-2 md:space-x-3 md:space-y-0">
        <HeadShot name="Maya Daader" title="Co-Chair" image={MayaDaader} quote="Hi, my name is Maya Daader and it is my first time co-chairing in mun. I'm in tenth grade and love debating and I hope to pursue law in the future. I'm so excited for this year's ALSMUN conference."/>
        <HeadShot name="Ziad Medhat" title="Co-Chair" image={ZiadMedhat} quote="Welcome to ALSMUNII! We can't wait to see you!"/>
    </section>
</section>

<header class="px-10">
    <h1 class=" text-4xl font-bold text-center mt-6"> Human Rights Council B </h1>
    <hr class="mb-2 mt-4">  
</header>
<section class="p-10 space-y-6">
    <GroupSection link={null} noReadMe={true} header="Omar ElHefnawy - Chair of HRC B" text={"While I close my mun career, Alsmun2 is going to kickstart a new chapter for us, change. I'm excited for my final mun and I hope you are too. HRC 4 EVER"} image={OmarElHefnawy} />
    <section class="space-x-0 space-y-2 md:grid md:grid-flow-col md:grid-cols-2 md:space-x-3 md:space-y-0">
        <HeadShot name="Nour Salah" title="Co-Chair" image={NourSalah} quote="Welcome to ALSMUNII! We can't wait to see you!"/>
        <HeadShot name="Habiba Kholeif" title="Co-Chair" image={HabibaKholeif} quote="Hi everyone! I'm Habiba and one of my favourite committees in MUN is HRC because it is generally about topics that I'm very passionate about. This is my very first MUN being a chair and I can't wait for it to start."/>
    </section>
</section>

   