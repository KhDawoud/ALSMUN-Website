<script lang="ts">
  import NavBar from "../../Components/NavBar.svelte";
  import GroupSection from "../../Components/GroupSection.svelte";
  import SDG from "../../../assets/Secretariat/Secretariat.jpg";
  import Banner from '../../Components/Banner.svelte';
  import AC from '../../../assets/AC.jpg';
  import OC from "../../../assets/OC.jpg";


</script>


<NavBar />

<Banner />

<main class="grid grid-flow-row grid-cols-1 space-y-5 m-5">
    <GroupSection noReadMe={false} header="Secretariat" link="/meet/secretariat" text={null} image={SDG} />
    <GroupSection noReadMe={false} header="Academic Committee" link="/meet/ac" text={null} image={AC} />
    <GroupSection noReadMe={false} header="Organising Committee" link="/meet/oc" text={null} image={OC}/>
</main>

