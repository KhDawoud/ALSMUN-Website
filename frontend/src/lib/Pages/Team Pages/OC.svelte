<script lang="ts">
    import NavBar from "../../Components/NavBar.svelte";
    import GroupSection from "../../Components/GroupSection.svelte";
    import Media from '../../../assets/OC/Media/Media.jpg';
    import Catering from '../../../assets/OC/Catering/Catering.jpg';
    import MahmoudHelmy from '../../../assets/Mahmoud Helmy.jpg';
    import OmarGabr from '../../../assets/Omar Gabr.jpg';
    import SaraTalaat from '../../../assets/Sara Talaat.jpg';
    import MostafaDawoud from '../../../assets/Mostafa Dawoud.jpg';
    import HalaNasr from '../../../assets/Hala Nasr.jpg';
    import HeadShot from "../../Components/HeadShot.svelte";
    import SoftwareTeam from "../../../assets/OC/SoftwareTeam/SoftwareTeam.jpg";
    import Banner from '../../Components/Banner.svelte';
</script>
  
  
  <NavBar />
  
  <Banner />
  
  <main class="grid grid-flow-row grid-cols-1 space-y-5 m-5">
      <GroupSection noReadMe={false} header="Software Team" link="/meet/oc/softwareteam" text={null} image={SoftwareTeam} />
      <GroupSection noReadMe={false} header="Media Team" link="/meet/oc/media" text={null} image={Media} />
      <GroupSection noReadMe={false} header="Catering Team" link='/meet/oc/catering' text={null} image={Catering} />
      <GroupSection noReadMe={true} header="Mahmoud Helmy - Head of Confrence Logistics" link={null} text={null} image={MahmoudHelmy} />
      <GroupSection noReadMe={true} header="Omar Gabr - Head of Aesthetics & Branding" link={null} text={null} image={OmarGabr} />
      
      <div class="row-span-1 grid grid-col-3 grid-flow-col space-x-2 w-75">
        <HeadShot name="Mostafa Dawoud" title="Room Setup" image={MostafaDawoud} quote="Live for the nights you'll never remember with the friends you'll never forget" />
        <HeadShot name="Hala Nasr" title="Awards & Certificates" image={HalaNasr} quote="You have to look through the rain to see the rainbow." />
        <HeadShot name="Sara Talaat" title="Head of Merchandise" image={SaraTalaat} quote="Life is what happens to you while you're busy making other plans." />
      </div>
  </main>