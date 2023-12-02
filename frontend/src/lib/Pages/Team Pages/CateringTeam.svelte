<script lang="ts">
    import NavBar from "../../Components/NavBar.svelte";
    import GroupSection from "../../Components/GroupSection.svelte";
    import YoussefElbarbary from "../../../assets/OC/Catering/Youssef ElBarbary - Catering.jpg"
    import LaylaElAbd from "../../../assets/OC/Catering/Layla El Abd - catering.jpg"
</script>

<NavBar />
<header class="px-10">
    <h1 class=" text-4xl font-bold text-center mt-10"> Our Catering Team </h1>
    <hr class="mb-10 mt-4">  
</header>
<main class="m-5 space-y-4">
    <GroupSection link={null} noReadMe={true} header="Youssef ElBarbary" text={null} image={YoussefElbarbary} />
    <GroupSection link={null} noReadMe={true} header="Layla ElAbd" text={null} image={LaylaElAbd} />
</main>