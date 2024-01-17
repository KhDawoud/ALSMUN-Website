<script lang="ts">
    import NavBar from "../../Components/NavBar.svelte";
    import GroupSection from "../../Components/GroupSection.svelte";
    import HeadShot from "../../Components/HeadShot.svelte";
    import KarimElguindy from "../../../assets/AC/GA-A/Karim Elguindy- GA A chair.jpg"
    import LaylaMourad from "../../../assets/AC/GA-A/Layla Mourad - GA A cochair.jpg"
    import MalakShawky from "../../../assets/AC/GA-B/Malak Shawky-GAB cochair.jpg"
    import CynthiaEzzi from "../../../assets/AC/GA-B/Cynthia Ezzi - GAB  co chair.jpg"
    import PlaceHolder from "../../../assets/PlaceHolder.jpeg"
</script>
  

    <NavBar />
    
    <header class="px-10">
        <h1 class=" text-4xl font-bold text-center mt-10"> General Assembly A </h1>
        <hr class="mb-2 mt-4">  
    </header>
    <section class="p-10 space-y-6">
        <GroupSection link={null} noReadMe={true} header="Karim ElGuindy - Chair of GA A" text={null} image={KarimElguindy} />
        <section class="space-x-0 space-y-2 md:grid md:grid-flow-col md:grid-cols-2 md:space-x-3 md:space-y-0">
            <HeadShot name="Layla Mourad" title="Co-Chair" image={LaylaMourad} quote="With determination anything is achievable"/>
            <HeadShot name="Youssef Sheriff" title="Co-Chair" image={PlaceHolder} quote="Sometimes all you need is a little imagination"/>
        </section>
    </section>
    
    <header class="px-10">
        <h1 class=" text-4xl font-bold text-center mt-6"> General Assembly B </h1>
        <hr class="mb-2 mt-4">  
    </header>
    <section class="p-10 space-y-6">
        <GroupSection link={null} noReadMe={true} header="Omar Fazary - Chair of GA B" text={null} image={PlaceHolder} />
        <section class="space-x-0 space-y-2 md:grid md:grid-flow-col md:grid-cols-2 md:space-x-3 md:space-y-0">
            <HeadShot name="Malak Shawky" title="Co-Chair" image={MalakShawky} quote="With determination anything is achievable"/>
            <HeadShot name="Cynthia Ezzi" title="Co-Chair" image={CynthiaEzzi} quote="Sometimes all you need is a little imagination"/>
        </section>
    </section>