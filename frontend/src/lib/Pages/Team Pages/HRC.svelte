<script lang="ts">
    import NavBar from "../../Components/NavBar.svelte";
    import GroupSection from "../../Components/GroupSection.svelte";
    import HeadShot from "../../Components/HeadShot.svelte";
    import SalmaSaber from "../../../assets/AC/HRC-A/Salma Saber - HRC A chair.jpg"
    import MayaDaader from "../../../assets/AC/HRC-A/Maya Daader - HRC A co chair.jpg"
    import ZiadMedhat from "../../../assets/AC/HRC-A/Ziad Medhat - HRC A co chair.jpg"
    import OmarElHefnawy from "../../../assets/AC/HRC-B/Omar Elhefnawy - HRC B chair.jpg"
    import NourSalah from "../../../assets/AC/HRC-B/Nour Salah - HRC B co chair.jpg"
    import HabibaKholeif from "../../../assets/AC/HRC-B/Habiba Kholeif - HRC B co chair.jpg"
</script>
  

<NavBar />
<header class="px-10">
    <h1 class=" text-4xl font-bold text-center mt-10"> Human Rights Council A </h1>
    <hr class="mb-2 mt-4">  
</header>
<section class="p-10 space-y-6">
    <GroupSection link={null} noReadMe={true} header="Salma Saber - Chair of HRC A" text={null} image={SalmaSaber} />
    <section class="grid grid-flow-col grid-cols-2 space-x-3">
        <HeadShot name="Maya Daader" title="Co-Chair" image={MayaDaader} quote="With determination anything is achievable"/>
        <HeadShot name="Ziad Medhat" title="Co-Chair" image={ZiadMedhat} quote="Sometimes all you need is a little imagination"/>
    </section>
</section>

<header class="px-10">
    <h1 class=" text-4xl font-bold text-center mt-6"> Human Rights Council B </h1>
    <hr class="mb-2 mt-4">  
</header>
<section class="p-10 space-y-6">
    <GroupSection link={null} noReadMe={true} header="Omar ElHefnawy - Chair of HRC B" text={null} image={OmarElHefnawy} />
    <section class="grid grid-flow-col grid-cols-2 space-x-3">
        <HeadShot name="Nour Salah" title="Co-Chair" image={NourSalah} quote="With determination anything is achievable"/>
        <HeadShot name="Habiba Kholeif" title="Co-Chair" image={HabibaKholeif} quote="Sometimes all you need is a little imagination"/>
    </section>
</section>

   