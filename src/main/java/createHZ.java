import com.hazelcast.core.Hazelcast;
import com.hazelcast.core.HazelcastInstance;

/**
 * Created by Esref Ozturk <esrefozturk93@gmail.com> on 08.07.2014.
 */
public class createHZ {
    public static void main(String[] args)
    {
        HazelcastInstance hz = Hazelcast.newHazelcastInstance();
    }
}