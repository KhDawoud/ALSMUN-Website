<script lang="ts">
    import NavBar from "../../Components/NavBar.svelte";
    import HeadShot from "../../Components/HeadShot.svelte";
    import OmarEzzi from "../../../assets/AC/ECOSOC-A/Omar Elezzi- ECOSOC A chair.jpg"
    import SalmaShayal from "../../../assets/AC/ECOSOC-A/Salma Shayal - ECOSOC A cochair.jpg"
    import AdamYoussef from "../../../assets/AC/ECOSOC-A/Adam Youssef - ECOSOC A co chair.jpg"
    import AlaaHashem from "../../../assets/AC/ECOSOC-B/Alaa Hashem - Chair of ECOSOC B.jpg"
    import HabibaRaslan from "../../../assets/AC/ECOSOC-B/Habiba Raslan - ECOSOC B co chair.jpg"
    import MahmoudHelmy from "../../../assets/AC/ECOSOC-B/Mahmoud Helmy- ECOSOC B co chair.jpg"
    import GroupSection from "../../Components/GroupSection.svelte";
</script>
  

    <NavBar />

    <header class="px-10">
        <h1 class=" text-4xl font-bold text-center mt-10"> Economic & Social Council A </h1>
        <hr class="mb-2 mt-4">  
    </header>
    <section class="p-10 space-y-6">
        <GroupSection link={null} noReadMe={true} header="Omar Ezzi - Chair of ECOSOC A" text={null} image={OmarEzzi} />
        <section class="space-x-0 space-y-2 md:grid md:grid-flow-col md:grid-cols-2 md:space-x-3 md:space-y-0">
            <HeadShot name="Salma Shayal" title="Co-Chair" image={SalmaShayal} quote="With determination anything is achievable"/>
            <HeadShot name="Adam Youssef" title="Co-Chair" image={AdamYoussef} quote="Sometimes all you need is a little imagination"/>
        </section>
    </section>
    
    <header class="px-10">
        <h1 class=" text-4xl font-bold text-center mt-6"> Economic & Social Council B </h1>
        <hr class="mb-2 mt-4">  
    </header>
    <section class="p-10 space-y-6">
        <GroupSection link={null} noReadMe={true} header="Alaa Hashem - Chair of ECOSOC B" text={null} image={AlaaHashem} />
        <section class="space-x-0 space-y-2 md:grid md:grid-flow-col md:grid-cols-2 md:space-x-3 md:space-y-0">
            <HeadShot name="Habiba Raslan" title="Co-Chair" image={HabibaRaslan} quote="With determination anything is achievable"/>
            <HeadShot name="Mahmoud Helmy" title="Co-Chair" image={MahmoudHelmy} quote="Sometimes all you need is a little imagination"/>
        </section>
    </section>
