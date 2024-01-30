<script lang="ts">
  import NavBar from "../../Components/NavBar.svelte";
  import GroupSection from "../../Components/GroupSection.svelte";
  import SDG from "../../../assets/Secretariat/Secretariat.jpg";
  import Banner from '../../Components/Banner.svelte';
  import AC from '../../../assets/Background/AC.jpg';
  import OC from "../../../assets/Background/OC.jpg";


</script>


<NavBar />

<Banner />

<main class="grid grid-flow-row grid-cols-1 space-y-5 m-5">
    <GroupSection noReadMe={false} header="Secretariat" link="/meet/secretariat" text={"ALSMUN is proud to be hosting its first open conference to students in Egypt this year. We have participated in many conferences around the world as delegates and chairs in the past and are ecstatic to bring Alssonian pride and spirit into the MUN community formally. ALSMUN will be a conference for delegates to grow intellectually and expand their understanding and comfort discussing international politics, reinforcing their social skills and public speaking."} image={SDG} />
    <GroupSection noReadMe={false} header="Academic Committee" link="/meet/ac" text={null} image={AC} />
    <GroupSection noReadMe={false} header="Organising Committee" link="/meet/oc" text={null} image={OC}/>
</main>

