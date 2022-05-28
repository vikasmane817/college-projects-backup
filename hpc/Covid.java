public class Covid{
    int Totalcount=0;
    int TotalRecovered=0;
    int currentcount=0;
    
    int total_count(){
        return Totalcount;
    }
    int total_recovered(){
        return TotalRecovered;
    }
    int current(){
        rerturn currentcount;
    }

    void increasecount(){
        Totalcount++;
        currentcount++;
    }
    void recovered(){
        currentcount--;
        TotalRecovered++;
    }

    public static void main(String args[])
    {
        Covid c= new Covid();
        System.out.println(c.total_count());
        c.increasecount();
        System.out.println(c.total_count());
        System.out.println(c.total_recovered());
        c.recovered();
        System.out.println(c.total_recovered());
    }

}