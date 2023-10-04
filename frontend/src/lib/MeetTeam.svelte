<script lang="ts">
  import NavBar from "./NavBar.svelte";
  import GroupSection from "./GroupSection.svelte";
  import SDG from "C:/Users/Admin/Desktop/MUN Website/frontend/src/assets/SDG.png";
  import Background from 'C:/Users/Admin/Desktop/MUN Website/frontend/src/assets/Team.jpg';
  import ICJ from 'C:/Users/Admin/Desktop/MUN Website/frontend/src/assets/ICJ.png';


</script>


<NavBar />

<div class ="flex items-center justify-center bg-cover bg-no-repeat bg-center w-full h-[30rem] px-10" style="background-image: url('{ Background}');">
  <div class ="sticky text-white text-7xl md:text-8xl font-extrabold text-center mt-20">Meet The Team</div>
</div>

<main class="grid grid-flow-row grid-cols-1 space-y-5 m-5">
    <GroupSection header="Secretariat" link="/meet/secretariat" text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." image={SDG} />
    <GroupSection header="Academic Committee" link="/meet/ac" text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." image={ICJ} />
    <GroupSection header="Organising Committee" link="/meet/oc" text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." image={Background} />
</main>

