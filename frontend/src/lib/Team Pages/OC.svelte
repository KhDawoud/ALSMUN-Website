<script lang="ts">
    import NavBar from "C:/Users/Admin/Desktop/MUN Website/frontend/src/lib/NavBar.svelte";
    import GroupSection from "C:/Users/Admin/Desktop/MUN Website/frontend/src/lib/GroupSection.svelte";
    import SDG from "C:/Users/Admin/Desktop/MUN Website/frontend/src/assets/SDG.png";
    import Background from 'C:/Users/Admin/Desktop/MUN Website/frontend/src/assets/Team.jpg';
    import ICJ from 'C:/Users/Admin/Desktop/MUN Website/frontend/src/assets/ICJ.png';
    import MahmoudHelmy from 'C:/Users/Admin/Desktop/MUN Website/frontend/src/assets/Mahmoud Helmy.jpg';
    import OmarGabr from 'C:/Users/Admin/Desktop/MUN Website/frontend/src/assets/Omar Gabr.jpg';
    import SaraTalaat from 'C:/Users/Admin/Desktop/MUN Website/frontend/src/assets/Sara Talaat.jpg';
    import MostafaDawoud from 'C:/Users/Admin/Desktop/MUN Website/frontend/src/assets/Mostafa Dawoud.jpg';
    import HalaNasr from 'C:/Users/Admin/Desktop/MUN Website/frontend/src/assets/Hala Nasr.jpg';
    import HeadShot from "../HeadShot.svelte";
  
  
  </script>
  
  
  <NavBar />
  
  <div class ="flex items-center justify-center bg-cover bg-no-repeat bg-center w-full h-[30rem] px-10" style="background-image: url('{ Background}');">
    <div class ="sticky text-white text-7xl md:text-8xl font-extrabold text-center mt-20">Meet The Team</div>
  </div>
  
  <main class="grid grid-flow-row grid-cols-1 space-y-5 m-5">
      <GroupSection header="Software Team" link="/home" text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." image={SDG} />
      <GroupSection header="Media Team" link="/home" text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." image={ICJ} />
      <GroupSection header="Catering Team" link='/home' text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." image={ICJ} />
      <div class="row-span-1 grid grid-cols-3 grid-flow-col space-x-2">
        <HeadShot name="Mahmoud Helmy" title="Head of Confrence Logistics" image={MahmoudHelmy} quote="Live Every Day Like It's Your Last" />
        <HeadShot name="Omar Gabr" title="Head of Aesthetics & Branding" image={OmarGabr} quote="Yesterday is history, tomorrow a mystery and today is a gift" />
        <HeadShot name="Sara Talaat" title="Head of Merchandise" image={SaraTalaat} quote="Life is what happens to you while you're busy making other plans." />
      </div>
      <div class="row-span-1 grid grid-col-2 grid-flow-col space-x-2 px-48">
        <HeadShot name="Mostafa Dawoud" title="Room Setup" image={MostafaDawoud} quote="Live for the nights you'll never remember with the friends you'll never forget" />
        <HeadShot name="Hala Nasr" title="Awards & Certificates" image={HalaNasr} quote="You have to look through the rain to see the rainbow." />
      </div>
  </main>