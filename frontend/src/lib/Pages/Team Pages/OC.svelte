<script lang="ts">
    import NavBar from "../../Components/NavBar.svelte";
    import GroupSection from "../../Components/GroupSection.svelte";
    import Media from '../../../assets/OC/Media/Media.jpg';
    import Catering from '../../../assets/OC/Catering/Catering.jpg';
    import MahmoudHelmy from '../../../assets/Heads/Mahmoud Helmy.jpg';
    import OmarGabr from '../../../assets/Heads/Omar Gabr.jpg';
    import SaraTalaat from '../../../assets/Heads/Sara Talaat.jpg';
    import MostafaDawoud from '../../../assets/Heads/Mostafa Dawoud.jpg';
    import HalaNasr from '../../../assets/Heads/Hala Nasr.jpg';
    import HeadShot from "../../Components/HeadShot.svelte";
    import SoftwareTeam from "../../../assets/OC/SoftwareTeam/SoftwareTeam.jpg";
    import Banner from '../../Components/Banner.svelte';
</script>
  
  
  <NavBar />
  
  <Banner />
  
  <main class="grid grid-flow-row grid-cols-1 space-y-5 m-5 px-3">
      <GroupSection noReadMe={true} header="Mahmoud Helmy - Head of Confrence Logistics" link={null} text={null} image={MahmoudHelmy} />
      <GroupSection noReadMe={true} header="Omar Gabr - Head of Aesthetics & Branding" link={null} text={"Working as the head of aesthetics and branding with the other heads for ALSMUN has been a very enjoyable experience. Although we had many ups and downs and many nights were spent managing all requirements for the media team and aiding with logistic andademic procedures, ultimately working for the media team at alsmun has been very rewarding, as the branding and aesthetics part of mun conferences is often overlooked despite being equally as important as academics for delegate enjoyment. We hope you enjoy ALSMUN! "} image={OmarGabr} />
      <GroupSection noReadMe={false} header="Software Team" link="/meet/oc/softwareteam" text={null} image={SoftwareTeam} />
      <GroupSection noReadMe={false} header="Media Team" link="/meet/oc/media" text={null} image={Media} />
      <GroupSection noReadMe={false} header="Catering Team" link='/meet/oc/catering' text={null} image={Catering} />
      
      
      <div class="space-y-2 space-x-0 md:row-span-1 md:grid md:grid-col-3 md:grid-flow-col md:space-x-2 md:space-y-0 w-75">
        <HeadShot name="Mostafa Dawoud" title="Room Setup" image={MostafaDawoud} quote="" />
        <HeadShot name="Hala Nasr" title="Awards & Certificates" image={HalaNasr} quote="" />
        <HeadShot name="Sara Talaat" title="Head of Merchandise" image={SaraTalaat} quote="" />
      </div>
  </main>