<script lang="ts">
    import NavBar from "../../Components/NavBar.svelte";
    import HeadShot from "../../Components/HeadShot.svelte";
    import NourEldinNassar from "../../../assets/AC/SC/Nour eldin - Chair SC.jpg"
    import AhmedFraige from "../../../assets/AC/SC/Ahmed Fraige - Security Council cochair.jpg"
    import GroupSection from "../../Components/GroupSection.svelte";
  </script>

    <NavBar />
    <header class="px-10">
        <h1 class=" text-4xl font-bold text-center mt-10"> Security Council </h1>
        <hr class="mb-2 mt-4">  
    </header>
    <main class="md:grid md:grid-flow-col md:grid-cols-2 md:m-5 md:space-x-4 md:space-y-0 p-5 space-x-0 space-y-2">
        <HeadShot name="Nour Eldin Nassar" title="Chair of SC" image={NourEldinNassar} quote="With determination anything is achievable"/>
        <HeadShot name="Ahmed Fraige" title="Co-Chair of SC" image={AhmedFraige} quote="Sometimes all you need is a little imagination"/>
    </main>
  
    