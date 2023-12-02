<script lang="ts">
    import NavBar from "../../Components/NavBar.svelte";
    import HeadShot from "../../Components/HeadShot.svelte";
    import SelimElMeadawy from "../../../assets/OC/Media/Selim Meadawy - Media and Photography.jpg"
    import PlaceHolder from "../../../assets/PlaceHolder.jpeg"
    import GroupSection from "../../Components/GroupSection.svelte";
</script>
  

    <NavBar />
    <header class="px-10">
        <h1 class=" text-4xl font-bold text-center mt-10"> Our Media Team </h1>
        <hr class="mb-2 mt-4">  
    </header>
    <main class="grid grid-flow-row grid-rows-3 m-5 space-y-4 p-5">
        <HeadShot name="Selim ElMeadawy" title="Photographer" image={SelimElMeadawy} quote="With determination anything is achievable"/>
        <HeadShot name="Hussein Namek" title="Media Team" image={PlaceHolder} quote="Sometimes all you need is a little imagination"/>
        <HeadShot name="Magdi El Bittar" title="Media Team" image={PlaceHolder} quote="Sometimes all you need is a little imagination"/>
    </main>
    <main class=" grid-flow-row grid-rows-3 m-5 space-y-4 p-5">
          <GroupSection link={null} noReadMe={true} header="Selim ElMeadawy - Photographer" text={null} image={SelimElMeadawy} />
          <GroupSection link={null} noReadMe={true} header="Hussein Namek - Media Team" text={null} image={PlaceHolder} />
          <GroupSection link={null} noReadMe={true} header="Magdi El Bittar - Media Team" text={null} image={PlaceHolder} />
    </main>
