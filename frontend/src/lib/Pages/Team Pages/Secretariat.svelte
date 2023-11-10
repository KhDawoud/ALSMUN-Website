<script lang="ts">
    import NavBar from "../../Components/NavBar.svelte";
    import GroupSection from "../../Components/GroupSection.svelte";
    import SDG from "../../../assets/SDG.png";
    import ICJ from '../../../assets/ICJ.png';
    import Banner from "../../Components/Banner.svelte";
    import OC from "../../../assets/OC.jpg";
  
  
  </script>
  
  
  <NavBar />
  
  <Banner />
  
  <main class="grid grid-flow-row grid-cols-1 space-y-5 m-5">
      <GroupSection header="SDG" link="/home" text={null} image={SDG} />
      <GroupSection header="..." link="/home" text={null} image={ICJ} />
      <GroupSection header="..." link="/home" text={null} image={OC} />
  </main>